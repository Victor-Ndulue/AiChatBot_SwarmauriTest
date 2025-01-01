# Python LLM-Driven RAG Agent with TF-IDF Vector Store

This project demonstrates a Python-based implementation of a Retrieval-Augmented Generation (RAG) agent powered by an LLM, vector store, and conversational context. It uses the `swarmauri` library to integrate various components like document storage, an AI agent, and natural language interaction.

---

## Features

1. **Large Language Model (LLM) Integration**:
   - Uses the `GroqModel` from `swarmauri` to integrate pre-trained LLMs.
   - Dynamically filters allowed LLM models based on predefined criteria.

2. **TF-IDF Vector Store**:
   - Implements a simple document retrieval mechanism using TF-IDF.
   - Supports adding, updating, and retrieving documents.

3. **RAG Agent**:
   - Combines the LLM with vector store for efficient question answering.
   - Maintains conversational context using a `MaxSystemContextConversation`.

4. **Sample Queries**:
   - Demonstrates the capability of the RAG agent to answer complex questions based on provided documents.

---

## Project Structure

```plaintext
llm_project/
├── src/
│   ├── main.py           # Entry point for the project.
│   ├── models/           # LLM-related utilities and setup.
│   ├── vector_store/     # TF-IDF vector store implementation.
│   ├── agents/           # RAG Agent logic.
│   ├── conversations/    # Conversation context and handling.
│   └── documents/        # Document model and related classes.
├── requirements.txt      # Project dependencies.
├── .env                  # Environment variables for sensitive data.
└── README.md             # Project documentation.
```

---

## Prerequisites

- **Python 3.13.1**
- A `.env` file with the following structure:
  ```
  GROQ_API_KEY=<your_groq_api_key>
  ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Victor-Ndulue/AiChatBot_SwarmauriTest.git
   cd llm-project
   ```

2. [Optional] Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API key.

---

## Usage

1. Run the project:
   ```bash
   python src/main.py
   ```

2. Add documents to the vector store using the predefined lists or update them dynamically.

3. Query the RAG agent with sample or custom questions to retrieve contextually relevant answers.

---

## Key Components

### LLM Initialization
The `GroqModel` class integrates an LLM using an API key. It filters allowed models to ensure only approved ones are used.

### Vector Store
The `TfidfVectorStore` handles document storage and retrieval based on TF-IDF similarity.

### RAG Agent
The `RagAgent` combines LLM capabilities with the vector store for contextualized question answering.

---

## Dependencies

- `swarmauri` library for LLM, vector store, and message/conversation handling.
- `python-dotenv` for managing environment variables.

---

## Example Queries

- "I need help with choosing a career between frontend and backend engineering."
- "What are the differences between Frontend and Backend Engineering?"

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

Thanks to the creators of the `swarmauri` library and open-source contributors for enabling this project.
