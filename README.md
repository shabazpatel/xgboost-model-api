# Credit Approval Model

This model uses user transaction information to predict if the the user will be approved for a loan (binary classification). This repository has `python_api.py` file which loads a xgboost AI model and serves it as a RESTful API.

Example call is as follows,
```
curl http://0.0.0.0:5000/predict -X POST -d '{"Num_txns": [7], "total_amount": [4102.0], "largest_txns": [751.0],"no_months": [7],"num_card_txns": [1],"num_cash_cheque_txns": [6],"num_wallet_txns":[0],"num_deliveries": [7.0],"max_lpg_delivery_amount": [751.0],"total_delivery_amount": [4627.5],"Percentage_card_txns": [0.1428571429]}' -H 'Content-type: application/json'
```
Output,
```
{
  "result": 1
}
```
