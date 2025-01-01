from swarmauri.messages.concrete.SystemMessage import SystemMessage
from swarmauri.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation

def create_conversation(system_message, max_size=10):
    system_context = SystemMessage(content=system_message)
    return MaxSystemContextConversation(system_context=system_context, max_size=max_size)
