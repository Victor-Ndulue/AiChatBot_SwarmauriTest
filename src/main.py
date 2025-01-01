from config import API_KEY
from models.llm_model import initialize_llm
from vector_store.vector_store import initialize_vector_store
from documents.document_loader import load_documents, load_additional_documents
from conversations.conversation import create_conversation
from models.rag_agent import create_rag_agent

# Initialize LLM
llm = initialize_llm(api_key=API_KEY)

# Initialize Vector Store
documents = load_documents()
vector_store = initialize_vector_store(documents)

# Add additional documents
additional_documents = load_additional_documents()
vector_store.add_documents(additional_documents)

# Initialize Conversation
system_message = "You are Victor. A senior Software Engineer that assists entry-level developers"
conversation = create_conversation(system_message=system_message)

# Create RAG Agent
rag_agent = create_rag_agent(llm, conversation, vector_store)

# Sample Queries
sample_queries = [
    "I need help with choosing a career between frontend and backend engineering",
    "What are the differences between Frontend and Backend Engineering?",
]

for query in sample_queries:
    response = rag_agent.exec(query)
    print(f"Query: {query}\nRAG Agent Response: {response}\n")
