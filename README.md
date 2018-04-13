<h1>Tools for ViaBTC Exchange Server</h1>
<h2>Usage:</h2>
API:</br>
```python
import api.api_exchange.py
import requests, json

ip_exchange = "http://10.211.55.3:8080/"
response = requests.post(ip_exchange, data=json.dumps(payload), headers=headers)
print(json.loads(response.text))
```import api.api_exchange.py
import requests, json

ip_exchange = "http://10.211.55.3:8080/"
response = requests.post(ip_exchange, data=json.dumps(payload), headers=headers)
print(json.loads(response.text))
