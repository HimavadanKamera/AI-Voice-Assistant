import os
import subprocess


# SPECIAL WINDOWS APPS (IMPORTANT)
SPECIAL_APPS = {
    "whatsapp": "start whatsapp:",
    "microsoft store": "start ms-windows-store:",
    "copilot": "start microsoft-edge://?ux=copilot",
    "calculator": "calc",
    "notepad": "notepad",
    "paint": "mspaint",
    "cmd": "cmd",
    "powershell": "powershell",
    "task manager": "taskmgr",
    "file explorer": "explorer",
    "chrome": "chrome",
    "edge": "msedge",
    "visual studio code": "code",
    "vs code": "code"
}


def get_installed_apps():

    apps = {}

    paths = [
        os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs"),
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
    ]

    for path in paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".lnk"):
                    name = file.replace(".lnk", "").lower()
                    apps[name] = os.path.join(root, file)

    return apps


def open_app(app_name):

    app_name = app_name.lower().strip()


    # 1. SPECIAL APPS
    if app_name in SPECIAL_APPS:
        try:
            subprocess.Popen(SPECIAL_APPS[app_name], shell=True)
            return True
        except:
            pass


    # 2. START MENU APPS
    apps = get_installed_apps()

    for installed_app in apps:
        if app_name in installed_app:
            try:
                os.startfile(apps[installed_app])
                return True
            except:
                pass


    # 3. LAST TRY (SYSTEM COMMAND)
    try:
        subprocess.Popen(f"start {app_name}", shell=True)
        return True
    except:
        pass


    return False