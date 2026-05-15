from datetime import datetime

def get_time():

    now = datetime.now()

    return now.strftime(
        "%I:%M %p"
    )

def get_date():

    today = datetime.now()

    return today.strftime(
        "%d %B %Y"
    )