# Credit Approval Model

This model uses user transaction information to predict if the the user will be approved for a loan (binary classification). This repository has `python_api.py` file which loads a xgboost AI model and serves it as a RESTful API.

Example:-

CURL request,
```
curl http://0.0.0.0:5000/predict -X POST -d '{"Num_txns": [7], "total_amount": [4102.0], "largest_txns": [751.0],"no_months": [7],"num_card_txns": [1],"num_cash_cheque_txns": [6],"num_wallet_txns":[0],"num_deliveries": [7.0],"max_lpg_delivery_amount": [751.0],"total_delivery_amount": [4627.5],"Percentage_card_txns": [0.1428571429]}' -H 'Content-type: application/json'
```

output from curl request,
```
{
  "result": 1
}
```

Load testing the API is performed using [Apache Bench tool](http://httpd.apache.org/docs/2.2/programs/ab.html)
```
Shabazs-MacBook-Pro:~ Shabaz$ ab -p data.json -T application/json -c 10 -n 1000 http://ec2-xx-xx-xx-xx.us-west-1.compute.amazonaws.com:5000/predict 
This is ApacheBench, Version 2.3 <$Revision: 1663405 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking ec2-xx-xx-xx-xx.us-west-1.compute.amazonaws.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.12.2
Server Hostname:        ec2-xx-xx-xx-xx.us-west-1.compute.amazonaws.com
Server Port:            5000

Document Path:          /predict
Document Length:        18 bytes

Concurrency Level:      10
Time taken for tests:   6.178 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      164000 bytes
Total body sent:        480000
HTML transferred:       18000 bytes
Requests per second:    161.86 [#/sec] (mean)
Time per request:       61.783 [ms] (mean)
Time per request:       6.178 [ms] (mean, across all concurrent requests)
Transfer rate:          25.92 [Kbytes/sec] received
                        75.87 kb/s sent
                        101.79 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       12   26  14.9     22     196
Processing:    18   35  18.7     29     215
Waiting:       16   34  17.9     28     215
Total:         35   61  29.6     51     266

Percentage of the requests served within a certain time (ms)
  50%     51
  66%     56
  75%     61
  80%     67
  90%     93
  95%    117
  98%    156
  99%    201
 100%    266 (longest request)
```

Here data.json contains following data,
```
{"num_cash_cheque_txns": [6], "Percentage_card_txns": [0.1428571429], "num_card_txns": [1], "no_months": [7], "num_deliveries": [7.0], "largest_txns": [751.0], "num_wallet_txns": [0], "Num_txns": [7], "total_amount": [4102.0], "total_delivery_amount": [4627.5], "max_lpg_delivery_amount": [751.0]}
```
