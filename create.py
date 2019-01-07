import requests

url = "https://obriand.fr/d/operation/create.php"

payload = "{\n    \"account\": \"bqe2\",\n    \"date\": \"2018-12-13\",\n    \"amount\": 23,\n    \"description\": \"test des 1\",\n    \"tags\": \"test tag 1\"\n}"
headers = {
    'PASS': "go17",
    'cache-control': "no-cache" }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
