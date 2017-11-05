import json
import uuid
import pytest
import datetime
from celery.result import AsyncResult
from celery_init import celery_app
from tasks import predict

TEST_TYPE='celery'

def test_predict():

    data = {'Num_txns': [6], 'total_amount': [1.010000e+05], 'largest_txns': [4.000000e+04],'no_months': [2],'num_card_txns': [6],'num_cash_cheque_txns': [0],'num_wallet_txns':[0],'num_deliveries': [0.0],'max_lpg_delivery_amount': [0.0],'total_delivery_amount': [0.0],'Percentage_card_txns': [1.000000]}

    if TEST_TYPE == 'celery':
        args = [data]
        task = celery_app.send_task('tasks.predict', args=args)
        result = task.wait()
    else:
        result = predict(data)
    print result, "result"

test_predict()
