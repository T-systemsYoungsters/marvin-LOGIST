import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def login ():
  auth = {
    'emailAddress': 'marvin 8 1658927863978 u0@wa',
    'password': 'Test12345678'
    }

  login = requests.post(BASEURL + '/authentication/login', json=auth)   

  loginResult = json.loads(login.text)

  organizationSiteKey = loginResult['organizations'][0]['sites'][0]['_key']
  organizationKey = loginResult['organizations'][0]['_key']

  return {'sessionId':loginResult['sessionId'],'organizationSiteKey':organizationSiteKey,'organizationKey':organizationKey}