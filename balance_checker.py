import subprocess, json, time, requests
import random
import jsonschema
from jsonrpcclient.http_client import HTTPClient

ip_exchange = "http://10.211.55.3:8080/"
coin_daemon_path = ["./litecoin-cli -regtest getinfo"]
#headers = {'content-type': 'application/json'}
last = 0
user_id='128'
coin = "BTC"

payload = {
  "method": "balance.query",
  "params": [int(user_id)],
  "jsonrpc": "2.0",
  "id": 0,
}

while True:
    json_output = subprocess.Popen(coin_daemon_path, stdout=subprocess.PIPE, shell=True)
    (out, err) = json_output.communicate()
    json_output_parsed = json.loads(out.decode('utf-8'))
    print(json_output_parsed["balance"])
    client = HTTPClient(ip_exchange)
    current_balance = json_output_parsed["balance"]
    try:
        if json_output_parsed["balance"] != last:
            print("!= balance")
            last = current_balance
            #response = requests.post(ip_exchange, data=json.dumps(payload), headers=headers)
            #print(json.loads(response.text)["result"]["BTC"]["available"])
            client.send('{"method": "balance.update", "params": [' + user_id + ', "' + coin + '", "deposit", ' + str(
                random.randrange(9999999)) + ', "' + str(current_balance) + '", {}], "id": 11000}',
                        headers={'Content-Type': 'application/json-rpc'})
        else:
            pass
    except jsonschema.exceptions.ValidationError:
        pass
    time.sleep(5)
