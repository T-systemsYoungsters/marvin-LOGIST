from login import *
from deliverynote import *
from supplychain import *
from deliverynotebundle import *
from loadcarriertemplate import *
from loadcarrier import *
from driverdetails import *
from checkout import *

logindata = login()
sessionId=logindata['sessionId']
organizationSiteKey=logindata['organizationSiteKey']
organizationKey=logindata['organizationKey']

deliveryNoteKey = create_deliveryNote(sessionId,organizationSiteKey)

supplychaindata = get_supplychain(sessionId,organizationSiteKey)
consignorkey=supplychaindata['consignorkey']
carrierkey=supplychaindata['carrierkey']
consigneekey=supplychaindata['consigneekey']

deliveryNoteBundleKey = create_deliverynotebundle(sessionId,consignorkey,carrierkey,consigneekey,deliveryNoteKey,organizationSiteKey)

loadCarrierTemplateKey = get_loadcarriertemplate(sessionId, organizationKey)

create_loadcarrier(sessionId,loadCarrierTemplateKey,organizationSiteKey,deliveryNoteBundleKey,deliveryNoteKey)

set_driverdetails(sessionId,carrierkey,consigneekey,consignorkey,organizationSiteKey,deliveryNoteBundleKey)

checkout(sessionId,deliveryNoteBundleKey,organizationSiteKey)