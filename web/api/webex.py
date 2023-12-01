import json
import os

import requests

from .azure import summeriseWebex

# your Webex Teams API token
WEBEX_TOKEN = str(os.environ["WEBEX_TOKEN"])


# your space ID
def get_roomid():
    url = "https://webexapis.com/v1/rooms"

    headers = {
        "Authorization": f"Bearer {WEBEX_TOKEN}",
        "Content-Type": "application/json",
    }
    r_id = []
    count = 0

    while url:
        if count == 5:
            break
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            rooms = response.json()["items"]
            for room in rooms:
                if count == 5:
                    break
                if room["type"] != None:
                    if room["type"] == "group":
                        count += 1
                        r_id.append(room["id"])
                else:
                    continue
            # check if there's a next page
            link_header = response.headers.get("Link")
            if link_header:
                # extract the next page URL
                url = link_header.split(";")[0].strip("<>")
            else:
                url = None
        else:
            print(f"Failed to get rooms: {response.content}")
            url = None
    return r_id


def get_messages():
    r_id = get_roomid()
    if r_id == None or len(r_id) == 0:
        return "Error"

    headers = {
        "Authorization": "Bearer {}".format(WEBEX_TOKEN),
        "Content-Type": "application/json",
    }

    webex_data = "Here is the list of all Webex Messages that came when the user was on leave, summerise it and share some insight maybe add useful links. Write all this properly\n"

    for id in r_id:
        url = f"https://webexapis.com/v1/messages?roomId={id}"
        response = requests.get(url, headers=headers)
        count = 0
        if response.status_code == 200:
            messages = response.json()["items"]
            for message in messages:
                count += 1
                if message.get("text"):
                    m = message["text"]
                    b = message["personEmail"]
                    webex_data += f"\nMessage From: {b}\nMessage Body: {m}\n"
                if count == 10:
                    break
        else:
            print(f"Failed to get messages: {response.content}")

    webex_data = summeriseWebex(webex_data=webex_data)
    return webex_data
