import requests

url = "https://obriand.fr/d/operation/list.php"

payload = ""
headers = {
    'PASS': "go17",
    'cache-control': "no-cache",
    'Postman-Token': "97c07c03-6622-46ed-a316-08b1969cb778"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
