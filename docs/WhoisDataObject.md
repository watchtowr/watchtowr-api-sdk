# WhoisDataObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | **str** | org | [optional] 
**city** | **str** | city | [optional] 
**name** | **str** | name | [optional] 
**state** | **str** | state | [optional] 
**dnssec** | **str** | dnssec | [optional] 
**emails** | [**WhoisDataObjectEmails**](WhoisDataObjectEmails.md) |  | [optional] 
**status** | [**WhoisDataObjectStatus**](WhoisDataObjectStatus.md) |  | [optional] 
**address** | **str** | address | [optional] 
**country** | **str** | country | [optional] 
**zipcode** | **str** | zipcode | [optional] 
**registrar** | **str** | registrar | [optional] 
**domain_name** | **str** | domain_name | [optional] 
**name_servers** | [**WhoisDataObjectNameServers**](WhoisDataObjectNameServers.md) |  | [optional] 
**referral_url** | **str** | referral_url | [optional] 
**whois_server** | **str** | whois_server | [optional] 
**creation_date** | **str** | creation_date | [optional] 
**expiration_date** | **str** | expiration_date | [optional] 

## Example

```python
from watchtowr_api.models.whois_data_object import WhoisDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisDataObject from a JSON string
whois_data_object_instance = WhoisDataObject.from_json(json)
# print the JSON string representation of the object
print(WhoisDataObject.to_json())

# convert the object into a dict
whois_data_object_dict = whois_data_object_instance.to_dict()
# create an instance of WhoisDataObject from a dict
whois_data_object_from_dict = WhoisDataObject.from_dict(whois_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


