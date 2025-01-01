from swarmauri.vector_stores.concrete.TfidfVectorStore import TfidfVectorStore

def initialize_vector_store(documents):
    vector_store = TfidfVectorStore()
    vector_store.add_documents(documents)
    return vector_store
