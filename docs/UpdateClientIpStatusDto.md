# UpdateClientIpStatusDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** | Updated asset status | 
**status_reason** | **str** | Reason of updated status | [optional] 

## Example

```python
from watchtowr_api.models.update_client_ip_status_dto import UpdateClientIpStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientIpStatusDto from a JSON string
update_client_ip_status_dto_instance = UpdateClientIpStatusDto.from_json(json)
# print the JSON string representation of the object
print UpdateClientIpStatusDto.to_json()

# convert the object into a dict
update_client_ip_status_dto_dict = update_client_ip_status_dto_instance.to_dict()
# create an instance of UpdateClientIpStatusDto from a dict
update_client_ip_status_dto_form_dict = update_client_ip_status_dto.from_dict(update_client_ip_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


