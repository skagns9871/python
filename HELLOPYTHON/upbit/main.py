import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import time
import pyupbit

import requests

access_key = 'C50xKD5IyefkNAFuc8CyjGxW2jd89uycr0uxDi1n'
secret_key = '2Hwq8NioxWuDqGiQUJ7dAR0VxHouYqZ8Rul4dqyx'
server_url = 'https://api.upbit.com'

temp = 99999;
while True :
    price = pyupbit.get_current_price("KRW-DOGE")
    if temp + temp * 0.03 < price :
        query = {
            'market': 'KRW-DOGE',
            'side': 'bid',
        #     'side': 'ask',
            'volume': '16',
            'price': price+3,
            'ord_type': 'limit',
        }
        query_string = urlencode(query).encode()
          
        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()
          
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }
        jwt_token = jwt.encode(payload, secret_key)
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}
          
        res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
        
        print("매수완료" + price)      
        print("매도중")
        time.sleep(30) 
       
        query = {
            'market': 'KRW-DOGE',
            # 'side': 'bid',
            'side': 'ask',
            'volume': '16',
            'price': price,
            'ord_type': 'limit',
        }
        query_string = urlencode(query).encode()
          
        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()
          
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }
        jwt_token = jwt.encode(payload, secret_key)
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}
          
        res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
        
        print("매도완료" + price)

        temp = price
        time.sleep(10) 
        
    else :
        print("----매수매수----")
        print("매수가" + temp)
        print("현재가" + price)
        print("--------")
        temp = price
        time.sleep(10) 
    
   
#      