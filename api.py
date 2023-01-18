import requests
import json
import time
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
for i in range(1,289):
	response = requests.get(url)
	result = response.json()
	print(result)
	time.sleep(300)