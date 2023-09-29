# watchtowr_api.BusinessUnitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_unit_details**](BusinessUnitApi.md#get_business_unit_details) | **GET** /api/client/business-unit/show/{id} | Get business unit details by business unit ID.
[**get_list_business_unit**](BusinessUnitApi.md#get_list_business_unit) | **GET** /api/client/business-unit/list | List Business Units.


# **get_business_unit_details**
> ClientBusinessUnitData get_business_unit_details(id)

Get business unit details by business unit ID.

### Example

* Bearer (Hex string) Authentication (bearer):
```python
import time
import os
import watchtowr_api
from watchtowr_api.models.client_business_unit_data import ClientBusinessUnitData
from watchtowr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = watchtowr_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Hex string): bearer
configuration = watchtowr_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with watchtowr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = watchtowr_api.BusinessUnitApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get business unit details by business unit ID.
        api_response = api_instance.get_business_unit_details(id)
        print("The response of BusinessUnitApi->get_business_unit_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessUnitApi->get_business_unit_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClientBusinessUnitData**](ClientBusinessUnitData.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | 404 Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_business_unit**
> PaginatedBusinessUnit get_list_business_unit(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search)

List Business Units.

### Example

* Bearer (Hex string) Authentication (bearer):
```python
import time
import os
import watchtowr_api
from watchtowr_api.models.paginated_business_unit import PaginatedBusinessUnit
from watchtowr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = watchtowr_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Hex string): bearer
configuration = watchtowr_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with watchtowr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = watchtowr_api.BusinessUnitApi(api_client)
    page = 1 # float | Pagination page (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)
    search = 'Singapore Business Unit' # str | Search business unit by name (optional)

    try:
        # List Business Units.
        api_response = api_instance.get_list_business_unit(page=page, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search)
        print("The response of BusinessUnitApi->get_list_business_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessUnitApi->get_list_business_unit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 
 **search** | **str**| Search business unit by name | [optional] 

### Return type

[**PaginatedBusinessUnit**](PaginatedBusinessUnit.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

