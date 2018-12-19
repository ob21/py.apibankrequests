import requests

url = "https://obriand.fr/d/operation/delete.php"

querystring = {"id":"1"}

payload = ""
headers = {
    'PASS': "go12",
    'cache-control': "no-cache",
    'Postman-Token': "eef7808f-2814-4920-8de7-ebbbce2cb021"
    }

response = requests.request("DELETE", url, data=payload, headers=headers, params=querystring)

print(response.text)
