import requests
import json
from login import *

BASEURL = 'https://dlsbackend.test.cloud4log.dev/api/v2'

data = login()
sessionId=data['sessionId']
organizationSiteKey=data['organizationSiteKey']
organizationKey=data['organizationKey']


headers = {
    'dlssessionId': sessionId,
    }

#get supplychain
supplyChainRequest = requests.get(BASEURL + f'/organization-sites/{organizationSiteKey}/supply-chains', headers=headers)   

supplyChainRequestResult = json.loads(supplyChainRequest.text)

consignorkey = supplyChainRequestResult['consignor'][0]['organizationSiteKey']
carrierkey = supplyChainRequestResult['carrier'][0]['organizationSiteKey']
consigneekey = supplyChainRequestResult['consignee'][0]['organizationSiteKey']

#create deliverynote
pdfheaders={
    'dlssessionId': sessionId,
    'content-type':'application/pdf'
    }

files = {'file': open('C:\\Users\\marvi\\Documents\\marvin-LOGIST\\DLS\\python request\\dlsapitest.pdf', 'rb')}
deliveryNoteRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-notes/pdf/shiny-pdf-file.pdf', headers=pdfheaders, files=files)
deliveryNoteRequestResult=json.loads(deliveryNoteRequest.text)

deliveryNoteKey = deliveryNoteRequestResult['_key']

#create deliverynotebundle
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

#get loadcarriertemplates
loadCarrierTemplateRequest = requests.get(BASEURL + f'/organizations/{organizationKey}/load-carrier-templates', headers=headers)

loadCarrierTemplateRequestResult = json.loads(loadCarrierTemplateRequest.text)

loadCarrierTemplateKey = loadCarrierTemplateRequestResult[0]['_key']

#create loadcarrier
loadCarrierRequestBody = {
  "templateKey": loadCarrierTemplateKey,
  "operation": "adoption",
  "quantity": 0,
  "damaged": True,
  "notice": "string"
}

loadCarrierRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles/{deliveryNoteBundleKey}/delivery-notes/{deliveryNoteKey}/load-carriers',headers=headers,json=loadCarrierRequestBody)

#patch deliverynotebundle "set driver details"
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

#checkout delivernotebundle
checkOutRequestBody = {
  "deliveryNoteBundleKeys": [deliveryNoteBundleKey],
  "carrierSignature": "string"
}

checkOutRequest = requests.post(BASEURL + f'/organization-sites/{organizationSiteKey}/delivery-note-bundles-checkout', headers=headers,json=checkOutRequestBody)

checkOutRequestResult = json.loads(checkOutRequest.text)

print(checkOutRequestResult)