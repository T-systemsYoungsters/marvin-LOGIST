import requests
import json
from login import *

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'


def get_supplychain(sessionId,organizationSiteKey):
    headers = {
        'dlssessionId': sessionId,
        }

    supplyChainRequest = requests.get(BASEURL + f'/organization-sites/{organizationSiteKey}/supply-chains', headers=headers)   

    supplyChainRequestResult = json.loads(supplyChainRequest.text)

    consignorkey = supplyChainRequestResult['consignor'][0]['organizationSiteKey']
    carrierkey = supplyChainRequestResult['carrier'][0]['organizationSiteKey']
    consigneekey = supplyChainRequestResult['consignee'][0]['organizationSiteKey']

    return {'consignorkey': consignorkey,'carrierkey':carrierkey,'consigneekey':consigneekey}