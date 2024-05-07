# UpdateClientFindingStatusRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Finding status | 

## Example

```python
from watchtowr_api.models.update_client_finding_status_request_body import UpdateClientFindingStatusRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientFindingStatusRequestBody from a JSON string
update_client_finding_status_request_body_instance = UpdateClientFindingStatusRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateClientFindingStatusRequestBody.to_json())

# convert the object into a dict
update_client_finding_status_request_body_dict = update_client_finding_status_request_body_instance.to_dict()
# create an instance of UpdateClientFindingStatusRequestBody from a dict
update_client_finding_status_request_body_from_dict = UpdateClientFindingStatusRequestBody.from_dict(update_client_finding_status_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


