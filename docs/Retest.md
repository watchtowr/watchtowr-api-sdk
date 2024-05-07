# Retest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retest_remaining** | **float** | The number of remaining test cases  | [optional] 
**current_retest** | [**FindingRetestResponseDto**](FindingRetestResponseDto.md) |  | 

## Example

```python
from watchtowr_api.models.retest import Retest

# TODO update the JSON string below
json = "{}"
# create an instance of Retest from a JSON string
retest_instance = Retest.from_json(json)
# print the JSON string representation of the object
print(Retest.to_json())

# convert the object into a dict
retest_dict = retest_instance.to_dict()
# create an instance of Retest from a dict
retest_from_dict = Retest.from_dict(retest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


