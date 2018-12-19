import requests

url = "https://obriand.fr/d/operation/search.php"

querystring = {"account":"bqe2","limit":"10","amount":"15","description":"test%20","offset":"1","amount_more_than":"20","amount_less_than":"13","tags_contains":"new","description_contains":"des"}

payload = ""
headers = {
    'PASS': "go17",
    'cache-control': "no-cache",
    'Postman-Token': "06b9dcb4-62c8-4310-802e-2a80955804e1"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
