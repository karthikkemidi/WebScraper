from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedder = SentenceTransformer('all-MiniLM-L6-v2')

class SimpleRAG:
    def __init__(self):
        self.texts = []
        self.embeddings = None
        self.index = None

    def add_texts(self, texts):
        self.texts.extend(texts)
        new_embeddings = embedder.encode(texts, convert_to_numpy=True)
        if self.embeddings is None:
            self.embeddings = new_embeddings
            self.index = faiss.IndexFlatL2(new_embeddings.shape[1])
            self.index.add(new_embeddings)
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings])
            self.index.add(new_embeddings)

    def search(self, query, top_k=3):
        query_embedding = embedder.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_embedding, top_k)
        results = [self.texts[i] for i in I[0]]
        return results

def split_text(text, chunk_size=500):
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) < chunk_size:
            current += " " + sentence
        else:
            chunks.append(current.strip())
            current = sentence
    if current:
        chunks.append(current.strip())
    return chunks
