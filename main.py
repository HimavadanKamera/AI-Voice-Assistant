from speech.wakeword import detect_wake_word
from speech.listen import listen_command
from speech.speak import speak

from ai.brain import ask_ai
from ai.memory_decider import should_store_memory
from ai.action_decider import decide_actions

from memory.vector_memory import store_memory, search_memories


# AUTOMATION IMPORTS
from automation.youtube import play_youtube
from automation.google_search import search_google
from automation.datetime_utils import get_time, get_date
from automation.screenshot import take_screenshot
from automation.dynamic_apps import open_app
from automation.dynamic_web import open_website
from automation.system_control import shutdown_pc, restart_pc, sleep_pc
from automation.volume_control import volume_up, volume_down, mute_volume, unmute_volume


conversation_history = []


speak("Jarvis is online")


while True:

    detect_wake_word()

    speak("Yes Hima")

    command = listen_command()

    print("Command:", command)

    if not command:
        continue


    cmd = command.lower().strip()


    # ---------------- QUICK SYSTEM COMMANDS ---------------- #

    if "time" in cmd:
        speak(f"The time is {get_time()}")
        continue

    elif "date" in cmd:
        speak(f"Today's date is {get_date()}")
        continue

    elif "screenshot" in cmd:
        filename = take_screenshot()
        speak(f"Screenshot saved as {filename}")
        continue

    elif "increase volume" in cmd:
        volume_up()
        speak("Volume increased")
        continue

    elif "decrease volume" in cmd:
        volume_down()
        speak("Volume decreased")
        continue

    elif "mute" in cmd:
        mute_volume()
        speak("Muted")
        continue

    elif "unmute" in cmd:
        unmute_volume()
        speak("Unmuted")
        continue

    elif "shutdown" in cmd:
        speak("Shutting down")
        shutdown_pc()
        continue

    elif "restart" in cmd:
        speak("Restarting")
        restart_pc()
        continue

    elif "sleep" in cmd:
        speak("Sleeping")
        sleep_pc()
        continue

    elif "exit" in cmd:
        speak("Goodbye Hima")
        break


    # ---------------- AI AGENT ACTIONS ---------------- #

    actions = decide_actions(command)

    handled = False

    for act in actions:

        action = act.get("action")
        value = act.get("value", "")

        if action == "open_app":
            speak(f"Opening {value}")
            success = open_app(value)
            if not success:
                open_website(value)
            handled = True

        elif action == "open_website":
            speak(f"Opening {value}")
            open_website(value)
            handled = True

        elif action == "search_google":
            speak(f"Searching {value}")
            search_google(value)
            handled = True

        elif action == "play_youtube":
            speak(f"Playing {value}")
            play_youtube(value)
            handled = True


    if handled:
        continue


    # ---------------- AI CONVERSATION ---------------- #

    conversation_history.append(f"User: {command}")

    memories = search_memories(command)

    response = ask_ai(
        "\n".join(conversation_history[-5:]),
        memories
    )

    print("Jarvis:", response)
    speak(response)

    conversation_history.append(f"Jarvis: {response}")

    if should_store_memory(command):
        store_memory(f"User: {command}")