# ServiceInformationCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**subject_common_name** | **str** | Subject Common Name | 
**subject_organisation** | **str** | Subject Organisation | 
**subject_alt_names** | **List[str]** | Subject Alt Names | 
**subject_country** | **str** | Subject Country | 
**issuer_common_name** | **str** | Issuer CommonName | 
**issuer_organisation** | **str** | Issuer Organisation | 
**issuer_country** | **str** | Issuer Country | 
**fingerprint** | **str** | Fingerprint | 
**public_key_info_alg** | **str** | PublicKeyInfoAlg | 
**public_key_info_size** | **str** | PublicKeyInfoSize | 
**status** | **str** |  | 
**created_at** | **datetime** | Discovery date | [optional] 

## Example

```python
from watchtowr_api.models.service_information_certificate import ServiceInformationCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInformationCertificate from a JSON string
service_information_certificate_instance = ServiceInformationCertificate.from_json(json)
# print the JSON string representation of the object
print(ServiceInformationCertificate.to_json())

# convert the object into a dict
service_information_certificate_dict = service_information_certificate_instance.to_dict()
# create an instance of ServiceInformationCertificate from a dict
service_information_certificate_from_dict = ServiceInformationCertificate.from_dict(service_information_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


