import requests
import os
import json
import pandas as pd  # Added this import

def create_embeddings(text_list):
    # Ensure this URL matches your Ollama version
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list, 
    })
    
    # Check if the request actually worked before parsing JSON
    if r.status_code != 200:
        print(f"Error from Ollama: {r.text}")
        return None
        
    response_data = r.json()
    
    # Ollama /api/embed returns "embeddings"
    return response_data.get("embeddings")

json_files = os.listdir("json") 
my_dict = []
chunk_id_counter = 0 

for file_name in json_files:
    if not file_name.endswith(".json"):
        continue
        
    with open(f"json/{file_name}", "r") as f:
        try:
            content = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping {file_name}: Invalid JSON format.")
            continue
    
    # Check if 'chunks' exists in the file
    if 'chunks' not in content:
        print(f"Skipping {file_name}: No 'chunks' key found.")
        continue

    # Extract text and get batch embeddings
    texts = [c["text"] for c in content['chunks']]
    embeddings = create_embeddings(texts)

    if embeddings is None:
        print(f"Skipping {file_name}: Failed to get embeddings.")
        continue

    # Correcting the loop to update the actual chunk data
    for i, c in enumerate(content['chunks']):
        c['chunk_id'] = chunk_id_counter
        # Use i to map the specific embedding to the specific chunk
        c['embedding'] = embeddings[i]
        
        my_dict.append(c)
        chunk_id_counter += 1

# Move these outside the loop if you want one big table at the end
df = pd.DataFrame.from_records(my_dict)
print(df.head()) # print(df) might be huge, .head() is cleaner