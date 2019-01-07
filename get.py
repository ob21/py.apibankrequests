import requests

url = "https://obriand.fr/d/operation/get.php"

querystring = {"id":10}

payload = ""
headers = {
    'PASS': "go17"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
