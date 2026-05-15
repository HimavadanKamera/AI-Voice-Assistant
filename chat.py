from ai.brain import ask_ai
from ai.memory_decider import should_store_memory

from memory.vector_memory import store_memory
from memory.vector_memory import search_memories


conversation_history = []


while True:

    question = input("You: ")


    if question.lower() == "exit":
        break


    # ADD TO CONVERSATION HISTORY
    conversation_history.append(f"User: {question}")


    # SEARCH RELEVANT MEMORIES
    memories = search_memories(question)


    # ASK AI WITH MEMORY + CONTEXT
    response = ask_ai(
        "\n".join(conversation_history[-5:]),  # last 5 messages
        memories
    )


    print("Jarvis:", response)


    # ADD RESPONSE TO HISTORY
    conversation_history.append(f"Jarvis: {response}")


    # SMART MEMORY STORAGE (AI decides)
    if should_store_memory(question):

        # CLEAN MEMORY BEFORE STORING
        cleaned = question.strip()

        store_memory(f"User: {cleaned}")