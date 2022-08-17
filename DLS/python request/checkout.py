import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def checkout(sessionId,deliveryNoteBundleKey,organizationSiteKey):

    headers = {
        'dlssessionId': sessionId,
        }

    checkOutRequestBody = {
    "deliveryNoteBundleKeys": [deliveryNoteBundleKey],
    "carrierSignature": "string"
    }

    checkOutRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles-checkout', headers=headers,json=checkOutRequestBody)

    checkOutRequestResult = json.loads(checkOutRequest.text)

    #accessToken = checkOutRequestResult['accessToken']
    
    print(checkOutRequestResult)