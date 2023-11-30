import requests
import json
import re
import html

# Constants
TENANT_ID = '86268193-d9e4-4b26-b74a-8e7f8b3f0dce'
CLIENT_ID = '96c1491c-ff19-4c1f-8439-afdda651cff2'
CLIENT_SECRET = 'nQJ8Q~7.J9hlNRirbTIUFAQ2REiLv6IVMHckBcOq'
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
ENDPOINT = 'https://graph.microsoft.com/v1.0/me/mailfolders/inbox/messages'
SCOPES = ['https://graph.microsoft.com/.default']

USER_ID = 'srashett@cresqa.onmicrosoft.com' # Replace with your user id or user principal name
ENDPOINT = f'https://graph.microsoft.com/v1.0/users/{USER_ID}/mailfolders/inbox/messages?$filter=isRead eq false'
SCOPES = ['https://graph.microsoft.com/.default']

def get_access_token(client_id, client_secret, authority):
    token_url = f"{authority}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': ' '.join(SCOPES)
    }
    token_r = requests.post(token_url, data=token_data)
    token = token_r.json().get('access_token')
    return token

def get_messages(access_token, endpoint):
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    r = requests.get(endpoint, headers=headers)
    #return r.json()
    return [{'subject': message['subject'], 'content': html.unescape(re.sub('<[^<]+?>', '', message['body']['content'])).replace('\u00a0', ' ').replace('\u202f', ' ').replace('\r\n', '\n')} for message in r.json().get('value', [])]
def main():
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, AUTHORITY)
    messages = get_messages(access_token, ENDPOINT)
    #print(json.dumps(messages, indent=4))
    with open('data.json', 'w') as f:
         json.dump(messages, f)

if __name__ == "__main__":
    main()
