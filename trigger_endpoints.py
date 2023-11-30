import json
import requests

llama2_endpoint = "http://localhost:8000/generate"
mistral_endpoint = "http://localhost:8001/generate"

query = "How to balance work-life balance working in Corporate?"

payload = json.dumps({
    "prompt": query,
    "temperature": 0.5,
    "top_k": 1,
    "top_p": 1.0,
    "max_tokens": 256,
    "frequency_penalty": 1.4
    }
)

headers = {
    "Content-Type": "application/json"
}
request = requests.request("POST", llama2_endpoint, headers=headers, data=payload, verify=False).json()
llama2_generated_answer = request
print(llama2_generated_answer)

request = requests.request("POST", mistral_endpoint, headers=headers, data=payload, verify=False).json()
mistral_generated_answer = request
print(mistral_generated_answer)
