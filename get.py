import requests

url = "https://obriand.fr/d/operation/get.php"

querystring = {"id":10}

payload = ""
headers = {
    'PASS': "go16",
    'cache-control': "no-cache",
    'Postman-Token': "c32bab89-086a-4b16-bb3e-a9f7516c1455"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
