import requests

url = "https://obriand.fr/d/operation/update.php"

payload = "{\n    \"id\":3,\n    \"account\": \"test acc up\",\n    \"date\": \"2018-12-04\",\n    \"amount\": 15,\n    \"description\": \"test des\",\n    \"tags\": \"new tags\"\n}"
headers = {
    'PASS': "go16",
    'cache-control': "no-cache",
    'Postman-Token': "18cf4c8a-57d5-41a3-b17c-8c2c46906fe5"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
