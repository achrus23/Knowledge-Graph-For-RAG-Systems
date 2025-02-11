import requests

url = "http://127.0.0.1:8020/query"
headers = {
    "Content-Type": "application/json"
}
data = {
    "query": "What is AI?",
    "mode": "hybrid",
    "only_need_context": True
}

response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
