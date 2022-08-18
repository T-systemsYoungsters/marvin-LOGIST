import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'


def create_deliverynotebundle(sessionId,consignorkey,carrierkey,consigneekey,deliveryNoteKey,organizationSiteKey):
    
    headers = {
        'dlssessionId': sessionId,
        }

    deliveryNoteBundleRequestBody = {
        'name': 'string',
        'consignorKey': consignorkey,
        'carrierKey': carrierkey,
        'consigneeKey': consigneekey,
        'deliveryNoteKeys': [deliveryNoteKey]
    }

    deliveryNoteBundleRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles', headers=headers, json=deliveryNoteBundleRequestBody)

    deliveryNoteBundleRequestResult = json.loads(deliveryNoteBundleRequest.text)

    deliveryNoteBundleKey = deliveryNoteBundleRequestResult['_key']

    return deliveryNoteBundleKey