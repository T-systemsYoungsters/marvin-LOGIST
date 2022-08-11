import requests
import json


BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

dlssessionId = {
  'J89uMbIUM+/mMsp9BzMerSPcD3bnBftFAQLs0OT6eiGtYKcl+6mzTzOcqeGxgCPp5bps+4lrpudgF0F0/+z7sFxn43fuK99YivyUFVfgUqwIFa7RWAEfMbkVYj6rDBr3kpvZ/ml8lh2bS7HeIpBSsYPfZFT0OfB3u82ejDwzst0='
  }

r = requests.post(BASEURL + '/organization-sites/7247938/supply-chains',json=dlssessionId)   

print(r.url)
print(r.text)
print(r.status_code)