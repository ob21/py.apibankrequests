import requests

url = "https://obriand.fr/d/operation/search.php"

querystring = {"account":"bqe2","limit":"20","amount_more_than":"5"}

payload = ""
headers = {
    'PASS': "go17",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
