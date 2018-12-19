import requests

url = "https://obriand.fr/d/operation/get.php"

querystring = {"id":10}

payload = ""
headers = {
    'PASS': "go17"}

#response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
response = requests.get("https://obriand.fr/d/operation/get.php?id=10", headers=headers) 

print(response.text)
