# PaginatedClientMobileApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientMobileApp]**](ClientMobileApp.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_mobile_app import PaginatedClientMobileApp

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientMobileApp from a JSON string
paginated_client_mobile_app_instance = PaginatedClientMobileApp.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientMobileApp.to_json())

# convert the object into a dict
paginated_client_mobile_app_dict = paginated_client_mobile_app_instance.to_dict()
# create an instance of PaginatedClientMobileApp from a dict
paginated_client_mobile_app_from_dict = PaginatedClientMobileApp.from_dict(paginated_client_mobile_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


