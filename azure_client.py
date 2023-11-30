from openai import AzureOpenAI
import json
import secret

client = AzureOpenAI(
    api_key=secret.api_key,
    api_version="2023-05-15",
    base_url="https://cloudsec-hackathon-apim.azure-api.net/openai/"
)