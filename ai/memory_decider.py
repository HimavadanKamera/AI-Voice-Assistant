import json
from ai.brain import ask_ai


def should_store_memory(text):

    prompt = f"""

You are an AI memory filter.

Decide if this message contains IMPORTANT personal information
that should be remembered long-term.

Store ONLY if it includes:
- name
- likes/dislikes
- preferences
- personal facts
- identity

Do NOT store:
- questions
- general knowledge
- random chat

Return ONLY JSON:

{{"store": true}} or {{"store": false}}

Message:
{text}
"""

    try:
        response = ask_ai(prompt)

        start = response.find("{")
        end = response.rfind("}") + 1

        return json.loads(response[start:end])["store"]

    except:
        return False