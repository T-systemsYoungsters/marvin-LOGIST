import requests
import json

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

def get_loadcarriertemplate(sessionId, organizationKey):

    headers = {
        'dlssessionId': sessionId,
        }
    loadCarrierTemplateRequest = requests.get(BASEURL + f'/organizations/{organizationKey}/load-carrier-templates', headers=headers)

    loadCarrierTemplateRequestResult = json.loads(loadCarrierTemplateRequest.text)

    loadCarrierTemplateKey = loadCarrierTemplateRequestResult[0]['_key']

    return loadCarrierTemplateKey