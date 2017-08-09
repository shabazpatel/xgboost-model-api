import requests
import json


def post_call(url, data):

    headers = {'Content-type': 'application/json'}
    data = json.dumps(data)
    res = requests.post(url, data=data, headers=headers)
    return res

url = 'http://localhost:5000/predict'
data = {'Num_txns': [6], 'total_amount': [1.010000e+05], 'largest_txns': [4.000000e+04],'no_months': [2],'num_card_txns': [6],'num_cash_cheque_txns': [0],'num_wallet_txns':[0],'num_deliveries': [0.0],'max_lpg_delivery_amount': [0.0],'total_delivery_amount': [0.0],'Percentage_card_txns': [1.000000]}        
response = post_call(url, data=data)

print response.json()
