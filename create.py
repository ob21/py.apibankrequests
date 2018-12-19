import requests

url = "https://obriand.fr/d/operation/create.php"

payload = "{\n    \"account\": \"bqe2\",\n    \"date\": \"2018-12-13\",\n    \"amount\": 23,\n    \"description\": \"test des 1\",\n    \"tags\": \"test tag 1\"\n}"
headers = {
    'PASS': "go16",
    'cache-control': "no-cache",
    'Postman-Token': "c742d7a0-11f1-4238-b022-732c76a26893"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
