import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def set_driverdetails(sessionId,carrierkey,consigneekey,consignorkey,organizationSiteKey,deliveryNoteBundleKey):

    headers = {
        'dlssessionId': sessionId,
        }

    deliveryNoteBundleDriverRequestBody = {
        "carrierEmailAddressOutgoing": "",
        "carrierKey": carrierkey,
        "carrierNameOutgoing": "Marvin Kühne",
        "carrierNumberPlateOutgoing": "HH CD 1001",
        "consigneeKey": consigneekey,
        "consignorKey": consignorkey,
        "name": ""
    }

    deliveryNoteBundleDriverRequest = requests.patch(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles/{deliveryNoteBundleKey}', headers=headers, json=deliveryNoteBundleDriverRequestBody)