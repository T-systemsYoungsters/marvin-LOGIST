import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def create_loadcarrier(sessionId,loadCarrierTemplateKey,organizationSiteKey,deliveryNoteBundleKey,deliveryNoteKey):
    headers = {
        'dlssessionId': sessionId,
        }

    loadCarrierRequestBody = {
        "templateKey": loadCarrierTemplateKey,
        "operation": "adoption",
        "quantity": 0,
        "damaged": True,
        "notice": "string"
        }

    loadCarrierRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles/{deliveryNoteBundleKey}/delivery-notes/{deliveryNoteKey}/load-carriers',headers=headers,json=loadCarrierRequestBody)