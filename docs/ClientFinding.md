# ClientFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**impact** | **str** |  | 
**finding_impact** | **str** |  | 
**tags** | [**List[ClientFindingImpactTag]**](ClientFindingImpactTag.md) |  | 
**evidence** | **str** |  | 
**recommendation** | **str** |  | 
**severity** | **str** |  | 
**cvssv3_score** | **float** |  | 
**cvssv3_metrics** | **str** |  | 
**status** | **str** |  | 
**created_at** | **object** |  | 
**affected** | **object** |  | 
**cve_id** | **str** |  | [optional] 
**epss_score** | **float** |  | [optional] 
**retest** | [**Retest**](Retest.md) |  | [optional] 
**finding_retests** | [**List[FindingRetestResponseDto]**](FindingRetestResponseDto.md) |  | 
**assigned_user** | [**ClientFindingAssignee**](ClientFindingAssignee.md) |  | 

## Example

```python
from watchtowr_api.models.client_finding import ClientFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFinding from a JSON string
client_finding_instance = ClientFinding.from_json(json)
# print the JSON string representation of the object
print(ClientFinding.to_json())

# convert the object into a dict
client_finding_dict = client_finding_instance.to_dict()
# create an instance of ClientFinding from a dict
client_finding_from_dict = ClientFinding.from_dict(client_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


