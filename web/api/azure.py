import os

from openai import AzureOpenAI

# Constants
AZURE_KEY = str(os.environ["AZURE_KEY"])

client = AzureOpenAI(
    api_key=AZURE_KEY,
    api_version="2023-05-15",
    base_url="https://cloudsec-hackathon-apim.azure-api.net/openai/",
)


def summerisePRs(pr_data):
    response = ""
    try:
        response = client.chat.completions.create(
            model="hack-gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "you are helpfull assistant, help a person who went a long leave to catch up with code and all PRs that went to code.",
                },
                {"role": "user", "content": pr_data},
                {
                    "role": "user",
                    "content": "Write a short summary in a single paragraph in maximum of 200 words. Also format the paragraph remove urls, brackets, symbols, also remove extra lines or new lines or /n",
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        response = str(e)

    return response


def summeriseMails(mail_data):
    response = ""
    try:
        response = client.chat.completions.create(
            model="hack-gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "you are helpfull assistant, help a person who went a long leave to catch up all Mails",
                },
                {"role": "user", "content": mail_data},
                {
                    "role": "user",
                    "content": "Write a short summary in a single paragraph in maximum of 200 words. Also format the paragraph remove urls, brackets, symbols, also remove extra lines or new lines or /n",
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        response = str(e)

    return response


def summeriseWebex(webex_data):
    response = ""
    try:
        response = client.chat.completions.create(
            model="hack-gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "you are helpfull assistant, help a person who went a long leave to catch up all his Cisco Webex work messages",
                },
                {"role": "user", "content": webex_data},
                {
                    "role": "user",
                    "content": "Write a short summary in a single paragraph in maximum of 200 words. Also format the paragraph remove urls, brackets, symbols, also remove extra lines or new lines or /n",
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        response = str(e)

    return response
