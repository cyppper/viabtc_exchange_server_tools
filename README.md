<h1>Tools for ViaBTC Exchange Server</h1>
<h2>Usage:</h2>
Get balance:</br>

```python
import api.api_exchange.py as ex
import requests, json

ip_exchange = "http://10.211.55.3:8080/"
headers = {'content-type': 'application/json'}

response = requests.post(ip_exchange, data=json.dumps(ex.balance.query(1)), headers=headers)
print(json.loads(response.text))
```

Buy me a beer :3 </br>
<h2>BTC: 1Px3sRDEcdC6mmpx4FofyeYnUFvcpmdYhp</h2>
<h2>LTC: LSNZkKq59oSHSHQmZMS4SncfMXoakePrKc</h2>
<h2>BCC: 1ZjJsE2aGYZyGJDjsPmfWyPKcF6qGhiaU</h2>
<h2>ETH (Only ETH, DONT SEND TOKENS): 0xabf2443445edc00e1c32a5b5f3c8479f51b9b4cb</h2>
