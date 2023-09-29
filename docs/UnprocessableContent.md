# UnprocessableContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status_code** | **float** |  | 
**errors** | **object** |  | 

## Example

```python
from watchtowr_api.models.unprocessable_content import UnprocessableContent

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessableContent from a JSON string
unprocessable_content_instance = UnprocessableContent.from_json(json)
# print the JSON string representation of the object
print UnprocessableContent.to_json()

# convert the object into a dict
unprocessable_content_dict = unprocessable_content_instance.to_dict()
# create an instance of UnprocessableContent from a dict
unprocessable_content_form_dict = unprocessable_content.from_dict(unprocessable_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


