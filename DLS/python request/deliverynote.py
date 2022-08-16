import requests
import json
from login import *
from supplychains import *

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

data = login()
sessionId=data['sessionId']
organizationSiteKey=data['organizationSiteKey']
organizationKey=data['organizationKey']


pdfheaders={
    'dlssessionId': sessionId,
    'content-type':'application/pdf'
    }

files = {'file': open('C:\\Users\\marvi\\Documents\\marvin-LOGIST\\DLS\\python request\\dlsapitest.pdf', 'rb')}
deliveryNoteRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-notes/pdf/shiny-pdf-file.pdf', headers=pdfheaders, files=files)
deliveryNoteRequestResult=json.loads(deliveryNoteRequest.text)

deliveryNoteKey = deliveryNoteRequestResult['_key']

print(deliveryNoteRequest.url)
print(deliveryNoteRequest.text)
print(deliveryNoteRequest.status_code)