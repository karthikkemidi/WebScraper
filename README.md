# AI Web Scraper (Gemini + RAG)

Extract and summarize website content and images using Google Gemini, Retrieval-Augmented Generation (RAG), and modern LLM techniques—all in a Streamlit web app.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://webscraper-kk.streamlit.app/)

---

## 🚀 Live Demo

👉 **Try it now:** [https://webscraper-kk.streamlit.app/](https://webscraper-kk.streamlit.app/)

---

## 🗂️ Features

- **Text Extraction:** Scrape main content from any public website.
- **Image Extraction:** Detect and display all images in a responsive, user-selectable grid.
- **RAG (Retrieval-Augmented Generation):** Retrieve and summarize the most relevant text chunks for your query using embeddings and FAISS.
- **Gemini Integration:** Use Google Gemini to answer your questions, grounded in retrieved context.
- **Explainability:** Transparent reasoning for all extractions.
- **Flexible UI:** Choose to extract text, images, or both; control image grid layout.

---

## 🏗️ Directory Structure

your_project/
├── ai_scraper.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── assets/
│ └── logo.png # Logo or static assets
└── utils/
├── init.py
├── multimodal_extractor.py # Text & image extraction
├── rag_integration.py # RAG logic (embeddings, retrieval)
└── explainability.py # Explainability functions

---

## ⚡ Quickstart (Local Setup)

1. **Clone the repo:**
    ```
    git clone https://github.com/<yourusername>/<repo-name>.git
    cd <repo-name>
    ```

2. **Install dependencies:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```
    streamlit run ai_scraper.py
    ```

---

## 🔑 Configuration

- **Gemini API Key:**  
  Enter your Google Gemini API key in the sidebar when prompted, or set it as a Streamlit secret.

---

## 🌐 Deployment

**Already deployed at:**  
[https://webscraper-kk.streamlit.app/](https://webscraper-kk.streamlit.app/)

**To deploy your own:**
1. Push your code to GitHub.
2. Go to [https://share.streamlit.io](https://share.streamlit.io).
3. Click "New app", select your repo and `ai_scraper.py` as the entry point.
4. Add your Gemini API Key as a secret if needed.
5. Deploy and share your app’s public URL!

---

## 🤖 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://ai.google.dev/)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

---

## 🤝 Contributing

Pull requests and issues are welcome!  
Please open an issue for feature requests or bug reports.


---

## 🙏 Acknowledgements

- [Streamlit Docs](https://docs.streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [OpenAI, HuggingFace, and the Python community](https://huggingface.co/)

---

