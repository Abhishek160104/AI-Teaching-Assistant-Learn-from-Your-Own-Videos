# 🎓 AI Teaching Assistant — Learn from Your Own Videos

> Turn any video lecture into a smart Q&A assistant using RAG + OpenAI Whisper

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-Whisper-green?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 🧠 What is this?

This project lets you build a **personal AI Teaching Assistant** from your own video lectures or educational content.

Simply drop your videos in a folder — and start asking questions about them using natural language. The system transcribes, embeds, and retrieves relevant content to generate accurate answers using a **RAG (Retrieval-Augmented Generation)** pipeline.

---

## ⚙️ How it Works

```
Video Files (.mp4)
      ↓
  [Step 1] Extract Audio → MP3
      ↓
  [Step 2] Transcribe Audio → JSON  (OpenAI Whisper)
      ↓
  [Step 3] Generate Embeddings → Joblib Vector Store
      ↓
  [Step 4] User Query → Relevant Prompt → LLM Answer
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Step 1 — Add Your Videos

```
Place all your video files inside the /videos folder.
```

### Step 2 — Convert Video to MP3

```bash
python video_to_mp3.py
```

Extracts audio from all videos in the `/videos` folder and saves `.mp3` files to `/audio`.

### Step 3 — Transcribe MP3 to JSON

```bash
python mp3_to_json.py
```

Uses **OpenAI Whisper** to transcribe each audio file into structured JSON with timestamps.

### Step 4 — Build Vector Store

```bash
python preprocess_json.py
```

Converts transcriptions into embeddings and saves a **Joblib pickle** file — your personal vector database.

### Step 5 — Ask Questions!

```bash
python query_engine.py
```

Enter any question related to your video content — the system retrieves the most relevant chunks and generates an answer using an LLM.

---

## 📁 Project Structure

```
ai-teaching-assistant/
│
├── videos/                  # Place your video files here
├── audio/                   # Auto-generated MP3 files
├── data/                    # JSON transcriptions
│
├── video_to_mp3.py          # Step 1: Video → MP3
├── mp3_to_json.py           # Step 2: MP3 → JSON (Whisper)
├── preprocess_json.py       # Step 3: JSON → Embeddings (Joblib)
├── query_engine.py          # Step 4: Query → LLM Answer
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| OpenAI Whisper | Speech-to-text transcription |
| Sentence Transformers / OpenAI Embeddings | Vector embeddings |
| Joblib | Vector store (pickle) |
| OpenAI GPT / any LLM | Answer generation |

---

## 💡 Use Cases

- 📚 Study from recorded college lectures
- 🎥 Index YouTube downloaded videos
- 🏫 Build a custom course assistant
- 🗣️ Search through meeting recordings

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature requests.

---

## 📄 License

MIT License — free to use and modify.

---

## 🌟 Star this repo if you found it useful!

*Built with ❤️ using Python and OpenAI Whisper*
