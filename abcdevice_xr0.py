import requests
import xmltodict
from config_info import router, Base_url



url =f"http://{router['ip']}:{router['port']}/api/running/l3vpn/abc/device"

print(url)

print('*' * 50 )

response = requests.get(url, auth=(router['username'], router['pw']), verify=False)

data = response.text.encode('utf8')

print(xmltodict.parse(data))
