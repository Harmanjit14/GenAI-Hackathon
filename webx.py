import requests
import json
import secret
# your Webex Teams API token
api_token = secret.webx_token
# your space ID
def get_roomid(space_name):
    url = "https://webexapis.com/v1/rooms"

    headers = {
        'Authorization': 'Bearer {}'.format(api_token),
        'Content-Type': 'application/json'
    }
    r_id=None
    while url:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            rooms = response.json()["items"]
            room_list=[room['id']  for room in rooms if room['title']==space_name]
            if room_list:
                r_id=room_list[0]
                break
            # check if there's a next page
            link_header = response.headers.get('Link')
            if link_header:
                # extract the next page URL
                url = link_header.split(';')[0].strip('<>')
            else:
                url = None
        else:
            print(f'Failed to get rooms: {response.content}')
            url = None
    return r_id

def get_messages(r_id):
    data=[]
    url = f"https://webexapis.com/v1/messages?roomId={r_id}"

    headers = {
        'Authorization': 'Bearer {}'.format(api_token),
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        messages = response.json()["items"]
        for message in messages:
            if message.get("text"):
                data.append({'message':message["text"], 'created_by': message["personEmail"], 'created_at': message["created"]})
                #print(f'Message: {message["text"]}, Created by: {message["personEmail"]}, Created at: {message["created"]}')
    else:
        print(f'Failed to get messages: {response.content}')
    return data

def main():
    r_id=get_roomid('CRES India Team') # do func call later
    messages=get_messages(r_id)
    if messages:
        with open('webx_data.json', 'w') as f:
            json.dump(messages, f)
main()