import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def login ():
  auth = {
    'emailAddress': 'marvin 8 1658927863978 u0@wa',
    'password': 'Test12345678'
    }

  r = requests.post(BASEURL + '/authentication/login', json=auth)   

  result = json.loads(r.text)

  organizationSiteKey = result['organizations'][0]['sites'][0]['_key']
  organizationKey = result['organizations'][0]['_key']

  return {'sessionId':result['sessionId'],'organizationSiteKey':organizationSiteKey,'organizationKey':organizationKey}
