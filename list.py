import requests

url = "https://obriand.fr/d/operation/list.php"

payload = ""
headers = {
    'PASS': "go17",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
