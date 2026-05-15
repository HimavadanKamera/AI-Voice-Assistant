import json

from ai.brain import ask_ai



def analyze_memory(user_message):

    prompt = f"""

You are a memory analyzer.

IMPORTANT:
Return ONLY valid JSON.
Do NOT explain anything.
Do NOT talk normally.

Possible outputs:

STORE MEMORY:
{{"type":"store","key":"favorite color","value":"gold"}}

RECALL MEMORY:
{{"type":"recall","key":"favorite color"}}

NORMAL CHAT:
{{"type":"normal"}}


Examples:

User: my favorite color is gold
Output:
{{"type":"store","key":"favorite color","value":"gold"}}

User: whats my favorite color
Output:
{{"type":"recall","key":"favorite color"}}

User: tell me a joke
Output:
{{"type":"normal"}}


Now analyze this:

User: {user_message}

ONLY RETURN JSON.
"""


    try:

        response = ask_ai(prompt)

        print("AI RAW:", response)


        start = response.find("{")

        end = response.rfind("}") + 1

        json_text = response[start:end]


        return json.loads(json_text)


    except Exception as e:

        print(e)

        return {
            "type": "normal"
        }