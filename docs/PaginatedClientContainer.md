# PaginatedClientContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientContainer]**](ClientContainer.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_container import PaginatedClientContainer

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientContainer from a JSON string
paginated_client_container_instance = PaginatedClientContainer.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientContainer.to_json())

# convert the object into a dict
paginated_client_container_dict = paginated_client_container_instance.to_dict()
# create an instance of PaginatedClientContainer from a dict
paginated_client_container_from_dict = PaginatedClientContainer.from_dict(paginated_client_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


