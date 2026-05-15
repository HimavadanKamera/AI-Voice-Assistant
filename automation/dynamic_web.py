import webbrowser

def open_website(site_name):

    site = site_name.replace(
        "open",
        ""
    ).strip()

    url = f"https://www.{site}.com"

    webbrowser.open(url)