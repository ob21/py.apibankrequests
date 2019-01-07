import requests

url = "https://obriand.fr/d/operation/delete.php"

querystring = {"id":"10"}

payload = ""
headers = {
    'PASS': "go17",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, data=payload, headers=headers, params=querystring)

print(response.text)
