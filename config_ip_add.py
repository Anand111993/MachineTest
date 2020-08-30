import requests
import xmltodict
from config_info import router, Base_url



url =f"http://{router['ip']}:{router['port']}/api/running/l3vpn/test/address"

payload = "<address>192.168.1.3</address>"

print(url)

print('*' * 50 )

requests.put(url, auth=(router['username'], router['pw']), verify=False, data = payload)

response = requests.get(url, auth=(router['username'], router['pw']), verify=False)

responses = response.text.encode('utf8')
print(responses)




