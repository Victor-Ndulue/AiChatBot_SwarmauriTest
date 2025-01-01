from swarmauri.agents.concrete.RagAgent import RagAgent

def create_rag_agent(llm, conversation, vector_store):
    return RagAgent(
        llm=llm,
        conversation=conversation,
        system_context=conversation.system_context.content,
        vector_store=vector_store,
    )
