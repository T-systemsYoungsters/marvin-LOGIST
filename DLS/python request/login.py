import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

auth = {
  'emailAddress': 'marvin 8 1658927863978 u0@wa',
  'password': 'Test12345678'
  }

r = requests.post(BASEURL + '/authentication/login', json=auth)   

print(r.url)
print(r.text)
print(r.status_code)