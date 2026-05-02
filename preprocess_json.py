import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

# REMOVED: from read_chunky import create_embeddings (This causes circular import)

def create_embeddings(text_list):
    try:
        r = requests.post("http://localhost:11434/api/embed", json={
            "model": "bge-m3",
            "input": text_list, 
        })
        if r.status_code != 200:
            print(f"Error from Ollama: {r.text}")
            return None
        return r.json().get("embeddings")
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

# Check if we should process files or load existing ones
if os.path.exists('embeddings.joblib'):
    print("Loading existing embeddings...")
    df = joblib.load('embeddings.joblib')
else:
    print("Processing JSON files...")
    json_files = os.listdir("json") 
    my_dict = []
    chunk_id_counter = 0 

    for file_name in json_files:
        if not file_name.endswith(".json"): continue
        
        with open(f"json/{file_name}", "r") as f:
            try:
                content = json.load(f)
            except: continue
        
        if 'chunks' not in content: continue

        texts = [c["text"] for c in content['chunks']]
        embeddings = create_embeddings(texts)

        if embeddings:
            for i, c in enumerate(content['chunks']):
                c['chunk_id'] = chunk_id_counter
                c['embedding'] = embeddings[i]
                my_dict.append(c)
                chunk_id_counter += 1
    
    df = pd.DataFrame.from_records(my_dict)
    joblib.dump(df, 'embeddings.joblib')

# --- Similarity Search ---
if not df.empty:
    print(df.head())
    incoming_query = input("\nAsk a question: ")
    
    q_embed_list = create_embeddings([incoming_query])
    
    if q_embed_list:
        question_embedding = q_embed_list[0]
        
        # Calculate similarities
        # np.vstack converts the list of arrays into one large 2D matrix
        similarities = cosine_similarity(np.vstack(df['embedding'].values), [question_embedding]).flatten()
        
        # Get top 3 indices
        top_results_count = 3
        max_indices = similarities.argsort()[::-1][:top_results_count]
        
        print("\n--- TOP MATCHES ---")
        new_df = df.iloc[max_indices].copy()
        new_df['score'] = similarities[max_indices]

        for index, item in new_df.iterrows():
            print(new_df[["title", "number", "text", "score","start","end"]])
  