# ClientActivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**description** | **object** | Description | 
**type** | **object** | Subject | 
**properties** | **object** | Log properties | [optional] 
**created_at** | **object** | Timestamp | [optional] 
**caused_by** | [**Causer**](Causer.md) |  | 

## Example

```python
from watchtowr_api.models.client_activity_log import ClientActivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of ClientActivityLog from a JSON string
client_activity_log_instance = ClientActivityLog.from_json(json)
# print the JSON string representation of the object
print(ClientActivityLog.to_json())

# convert the object into a dict
client_activity_log_dict = client_activity_log_instance.to_dict()
# create an instance of ClientActivityLog from a dict
client_activity_log_from_dict = ClientActivityLog.from_dict(client_activity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


