import requests
import xmltodict
from config_info import router, Base_url



url =f"http://{router['ip']}:{router['port']}/api/running/l3vpn/test/vlanId"

payload = "<vlanId>234</vlanId>"

print(url)

print('*' * 50 )

requests.put(url, auth=(router['username'], router['pw']), verify=False, data = payload)

response = requests.get(url, auth=(router['username'], router['pw']), verify=False)

responses = response.text.encode('utf8')
print(responses)

