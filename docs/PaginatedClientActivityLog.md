# PaginatedClientActivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientActivityLog]**](ClientActivityLog.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api.models.paginated_client_activity_log import PaginatedClientActivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientActivityLog from a JSON string
paginated_client_activity_log_instance = PaginatedClientActivityLog.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientActivityLog.to_json())

# convert the object into a dict
paginated_client_activity_log_dict = paginated_client_activity_log_instance.to_dict()
# create an instance of PaginatedClientActivityLog from a dict
paginated_client_activity_log_from_dict = PaginatedClientActivityLog.from_dict(paginated_client_activity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


