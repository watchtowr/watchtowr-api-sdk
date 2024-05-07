# UpdateClientNextGenAssetStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Target status to update | 
**status_reason** | **str** | Reason of updating status | [optional] 

## Example

```python
from watchtowr_api.models.update_client_next_gen_asset_status_dto import UpdateClientNextGenAssetStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientNextGenAssetStatusDto from a JSON string
update_client_next_gen_asset_status_dto_instance = UpdateClientNextGenAssetStatusDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientNextGenAssetStatusDto.to_json())

# convert the object into a dict
update_client_next_gen_asset_status_dto_dict = update_client_next_gen_asset_status_dto_instance.to_dict()
# create an instance of UpdateClientNextGenAssetStatusDto from a dict
update_client_next_gen_asset_status_dto_from_dict = UpdateClientNextGenAssetStatusDto.from_dict(update_client_next_gen_asset_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


