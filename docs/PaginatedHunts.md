# PaginatedHunts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Hunt]**](Hunt.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_hunts import PaginatedHunts

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHunts from a JSON string
paginated_hunts_instance = PaginatedHunts.from_json(json)
# print the JSON string representation of the object
print(PaginatedHunts.to_json())

# convert the object into a dict
paginated_hunts_dict = paginated_hunts_instance.to_dict()
# create an instance of PaginatedHunts from a dict
paginated_hunts_from_dict = PaginatedHunts.from_dict(paginated_hunts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


