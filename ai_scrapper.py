import streamlit as st
from utils.multimodal_extractor import extract_image_urls, extract_clean_main_text
from utils.rag_integration import SimpleRAG, split_text
from utils.explainability import explain_decision
import google.generativeai as genai

st.set_page_config(page_title="AI Web Scraper (Gemini + RAG)", page_icon="🕵️‍♂️", layout="wide")
st.title("AI Web Scraper (Gemini + RAG)")
st.caption("Extract raw content, Gemini+RAG answer, and images grid for any public website.")

# --- User selection for mode ---
mode = st.radio(
    "Select what you want to extract:",
    ["Text", "Images", "Both"],
    index=2,  # Default to 'Both'
)  # [2][3][4][7]

url = st.text_input("Enter the URL of the website you want to scrape")
user_prompt = ""
if mode in ["Text", "Both"]:
    user_prompt = st.text_input("What do you want to extract or summarize?")

gemini_api_key = ""
gemini_model = ""
if mode in ["Text", "Both"]:
    gemini_api_key = st.sidebar.text_input("Google Gemini API Key", type="password")
    gemini_model = st.sidebar.radio(
        "Gemini Model", ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"], index=0
    )

num_columns = 4
if mode in ["Images", "Both"]:
    num_columns = st.slider("Number of columns in image grid", min_value=2, max_value=8, value=4)

if st.button("Scrape") and url and (mode == "Images" or user_prompt):
    try:
        text, image_urls = "", []
        # --- TEXT EXTRACTION AND RAG+GEMINI ---
        if mode in ["Text", "Both"]:
            text = extract_clean_main_text(url)
            st.subheader("Raw Extracted Content")
            st.write(text[:2000] + ("..." if len(text) > 2000 else ""))

            chunks = split_text(text)
            rag = SimpleRAG()
            rag.add_texts(chunks)
            retrieved_chunks = rag.search(user_prompt, top_k=3)
            context = "\n\n".join(retrieved_chunks)
            st.subheader("RAG Retrieved Context")
            st.write(context)

            genai.configure(api_key=gemini_api_key)
            gemini = genai.GenerativeModel(gemini_model)
            gemini_prompt = (
                f"Given the following context extracted from a web page, answer the user's request as accurately as possible.\n"
                f"User request: {user_prompt}\n"
                f"Context:\n{context}"
            )
            gemini_response = gemini.generate_content(gemini_prompt)
            st.subheader("Gemini + RAG Answer")
            st.write(gemini_response.text)

        # --- IMAGES GRID ---
        if mode in ["Images", "Both"]:
            image_urls = extract_image_urls(url)
            st.subheader(f"Images Found ({len(image_urls)})")
            if image_urls:
                rows = (len(image_urls) + num_columns - 1) // num_columns
                for row in range(rows):
                    cols = st.columns(num_columns)
                    for col_idx in range(num_columns):
                        img_idx = row * num_columns + col_idx
                        if img_idx < len(image_urls):
                            with cols[col_idx]:
                                st.image(image_urls[img_idx], use_container_width=True)
            else:
                st.warning("No images found on this page.")

        # --- EXPLAINABILITY ---
        if mode in ["Text", "Both"]:
            explanation = explain_decision(text, image_urls, [], user_prompt)
            st.info(explanation)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter a website URL and required options, then click 'Scrape' to begin.")
