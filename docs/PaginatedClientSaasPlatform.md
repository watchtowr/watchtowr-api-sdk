# PaginatedClientSaasPlatform


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientSaasPlatform]**](ClientSaasPlatform.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_saas_platform import PaginatedClientSaasPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientSaasPlatform from a JSON string
paginated_client_saas_platform_instance = PaginatedClientSaasPlatform.from_json(json)
# print the JSON string representation of the object
print PaginatedClientSaasPlatform.to_json()

# convert the object into a dict
paginated_client_saas_platform_dict = paginated_client_saas_platform_instance.to_dict()
# create an instance of PaginatedClientSaasPlatform from a dict
paginated_client_saas_platform_form_dict = paginated_client_saas_platform.from_dict(paginated_client_saas_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


