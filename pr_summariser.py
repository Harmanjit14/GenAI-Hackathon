from openai import AzureOpenAI
import json
import secret

client = AzureOpenAI(
    api_key=secret.api_key,
    api_version="2023-05-15",
    base_url="https://cloudsec-hackathon-apim.azure-api.net/openai/"
)
with open('pr_data.json', 'r') as f:
    pr=json.load(f)

response = client.chat.completions.create(
    model="hack-gpt-4",  # model = "deployment_name".
    messages=[
        {"role": "system", "content": "you are helpfull assistant , helping person who went a long leave to ,catch up."},
        {"role": "user", "content": str(pr)},
        {"role": "user","content":"given a list of pr deatils in the format title and description , give list of  shor summary of them , if you think particular PR does not have important change you can skip them "}
    ]
)
print(response.choices[0].message.content)