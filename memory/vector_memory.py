import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="jarvis_memory"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


memory_counter = 0


# STORE MEMORY
def store_memory(text):

    global memory_counter

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(memory_counter)],
        embeddings=[embedding],
        documents=[text]
    )

    memory_counter += 1


# SEARCH MEMORY
def search_memories(query, n_results=2):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    filtered = []

    for doc, dist in zip(documents, distances):
        if dist < 1.2:   # similarity threshold
            filtered.append(doc)

    return filtered