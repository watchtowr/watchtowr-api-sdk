# SuspiciousDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 
**discovery_reason** | **str** | Discovery Reason | 
**status** | **str** |  | 
**whois_data** | [**List[WhoisData]**](WhoisData.md) |  | 
**created_at** | **datetime** | Discovery date | [optional] 

## Example

```python
from watchtowr_api.models.suspicious_domain import SuspiciousDomain

# TODO update the JSON string below
json = "{}"
# create an instance of SuspiciousDomain from a JSON string
suspicious_domain_instance = SuspiciousDomain.from_json(json)
# print the JSON string representation of the object
print(SuspiciousDomain.to_json())

# convert the object into a dict
suspicious_domain_dict = suspicious_domain_instance.to_dict()
# create an instance of SuspiciousDomain from a dict
suspicious_domain_from_dict = SuspiciousDomain.from_dict(suspicious_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


