import ollama


def ask_ai(question, memories=None):

    try:

        memory_context = ""

        if memories:
            memory_context = "\n".join(memories)


        prompt = f"""
You are Jarvis, a smart and natural AI assistant.

Rules:
- Use memory ONLY if it is directly relevant to the question.
- Ignore unrelated memories completely.
- NEVER mix different memories together.
- NEVER guess personal details.
- If the answer is not in memory, respond normally.
- If unsure about personal info, say: "I don't remember that yet."
- Keep answers short, clear, and human-like.
- Do not over-explain.

Memory:
{memory_context}

User:
{question}

Answer like a normal human:
"""


        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


    except Exception as e:
        print(e)
        return "Sorry Hima, something went wrong."