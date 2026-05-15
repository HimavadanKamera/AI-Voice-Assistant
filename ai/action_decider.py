import json
from ai.brain import ask_ai


def decide_actions(command):

    prompt = f"""

You are an AI assistant that converts user commands into actions.

Available actions:
1. open_app
2. open_website
3. search_google
4. play_youtube
5. none

Return JSON list.

Examples:

User: open chrome
Output:
[{{"action":"open_app","value":"chrome"}}]

User: open youtube and play songs
Output:
[
{{"action":"open_website","value":"youtube"}},
{{"action":"play_youtube","value":"songs"}}
]

User: tell me a joke
Output:
[{{"action":"none"}}]

Now convert:

User: {command}
"""

    try:
        response = ask_ai(prompt)

        start = response.find("[")
        end = response.rfind("]") + 1

        return json.loads(response[start:end])

    except:
        return [{"action": "none"}]