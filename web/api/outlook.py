import html
import os
import re

import requests

from .azure import summeriseMails

TENANT_ID = str(os.environ["TENANT_ID"])
CLIENT_ID = str(os.environ["CLIENT_ID"])
CLIENT_SECRET = str(os.environ["CLIENT_SECRET"])
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

SCOPES = ["https://graph.microsoft.com/.default"]


def get_access_token(client_id, client_secret, authority):
    token_url = f"{authority}/oauth2/v2.0/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": " ".join(SCOPES),
    }
    token_r = requests.post(token_url, data=token_data)
    token = token_r.json().get("access_token")
    return token


def get_messages(access_token, endpoint):
    headers = {"Authorization": f"Bearer {access_token}"}
    email_data = "Here is the list subject and body of all the mails that came when the user was on leave, summerise it and share some insight maybe add useful links. Write all this properly\n"

    try:
        r = requests.get(endpoint, headers=headers)
        for message in r.json().get("value", []):
            subject = (message["subject"],)
            body = (
                html.unescape(re.sub("<[^<]+?>", "", message["body"]["content"]))
                .replace("\u00a0", " ")
                .replace("\u202f", " ")
                .replace("\r\n", " "),
            )
            email_sample = f"\nEmail Subject: {subject}\nEmail Body: {body}\n"
            email_data += email_sample

    except Exception as e:
        return str(e)

    email_data = summeriseMails(mail_data=email_data)
    return email_data


def get_mails(start_date, end_date):
    USER_ID = "srashett@cresqa.onmicrosoft.com"  # Replace with your user id or user principal name
    ENDPOINT = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/mailfolders/inbox/messages?$filter=isRead eq false"

    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, AUTHORITY)
    email_data = get_messages(access_token, ENDPOINT)
    return email_data
