import json
from azure_client import client

with open('webx_data.json', 'r') as f:
    webx_messages=json.load(f)

response = client.chat.completions.create(
    model="hack-gpt-4",  # model = "deployment_name".
    messages=[
        {"role": "system", "content": "you are helpfull assistant , helping person who went a long leave to ,catch up using webx messages."},
        {"role": "user", "content": str(webx_messages)},
        {"role": "user","content":"given a list of messages a webex group in json format , filter the important one's which are important for me:srashett and give short summary of it, if any action from user side is required , create actionlist"}
    ]
)
print(response.choices[0].message.content)