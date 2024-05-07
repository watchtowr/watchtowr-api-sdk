# watchtowr_api.AssetSaaSPlatformsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_saas_platform_details**](AssetSaaSPlatformsApi.md#get_asset_saas_platform_details) | **GET** /api/client/assets/saasPlatform/show/{id} | Show the details of a specific SaaS Platform.
[**get_list_asset_saas_platforms**](AssetSaaSPlatformsApi.md#get_list_asset_saas_platforms) | **GET** /api/client/assets/saasPlatform/list | List all discovered SaaS Platforms, ordered by date identified.
[**update_asset_saas_platform_status**](AssetSaaSPlatformsApi.md#update_asset_saas_platform_status) | **PUT** /api/client/assets/saasPlatform/update-status/{id} | Update status of a specific SaaS platform asset.


# **get_asset_saas_platform_details**
> ClientSaasPlatformData get_asset_saas_platform_details(id, api_token)

Show the details of a specific SaaS Platform.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_saas_platform_data import ClientSaasPlatformData
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
    api_instance = watchtowr_api.AssetSaaSPlatformsApi(api_client)
    id = 3.4 # float | 
    api_token = 'api_token_example' # str | 

    try:
        # Show the details of a specific SaaS Platform.
        api_response = api_instance.get_asset_saas_platform_details(id, api_token)
        print("The response of AssetSaaSPlatformsApi->get_asset_saas_platform_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetSaaSPlatformsApi->get_asset_saas_platform_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **api_token** | **str**|  | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_asset_saas_platforms**
> PaginatedClientSaasPlatform get_list_asset_saas_platforms(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)

List all discovered SaaS Platforms, ordered by date identified.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_client_saas_platform import PaginatedClientSaasPlatform
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
    api_instance = watchtowr_api.AssetSaaSPlatformsApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    asset_name = 'example.slack.com' # str | Keyword search in a SaaS Platform URL (optional)
    statuses = ['verified,Third Party,Unregistered,Incorrect Identification,pending,VerifiedOutOfScope,VerifiedReducedAttack,Tracked'] # List[str] | Asset statuses (optional)
    business_unit_ids = '1,2,3' # str | Comma separated list of Business Unit IDs (optional)
    created_from = '2022-02-22 22:00:00' # datetime | created_at Date Range Beginning (optional)
    created_to = '2022-02-23 22:00:00' # datetime | created_at Date Range Ending (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | updated_at Date Range Beginning (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | updated_at Date Range Ending (optional)

    try:
        # List all discovered SaaS Platforms, ordered by date identified.
        api_response = api_instance.get_list_asset_saas_platforms(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)
        print("The response of AssetSaaSPlatformsApi->get_list_asset_saas_platforms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetSaaSPlatformsApi->get_list_asset_saas_platforms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 
 **asset_name** | **str**| Keyword search in a SaaS Platform URL | [optional] 
 **statuses** | [**List[str]**](str.md)| Asset statuses | [optional] 
 **business_unit_ids** | **str**| Comma separated list of Business Unit IDs | [optional] 
 **created_from** | **datetime**| created_at Date Range Beginning | [optional] 
 **created_to** | **datetime**| created_at Date Range Ending | [optional] 
 **updated_from** | **datetime**| updated_at Date Range Beginning | [optional] 
 **updated_to** | **datetime**| updated_at Date Range Ending | [optional] 

### Return type

[**PaginatedClientSaasPlatform**](PaginatedClientSaasPlatform.md)

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

# **update_asset_saas_platform_status**
> ClientSaasPlatformData update_asset_saas_platform_status(id, update_client_next_gen_asset_status_dto)

Update status of a specific SaaS platform asset.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_saas_platform_data import ClientSaasPlatformData
from watchtowr_api.models.update_client_next_gen_asset_status_dto import UpdateClientNextGenAssetStatusDto
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
    api_instance = watchtowr_api.AssetSaaSPlatformsApi(api_client)
    id = 3.4 # float | 
    update_client_next_gen_asset_status_dto = watchtowr_api.UpdateClientNextGenAssetStatusDto() # UpdateClientNextGenAssetStatusDto | 

    try:
        # Update status of a specific SaaS platform asset.
        api_response = api_instance.update_asset_saas_platform_status(id, update_client_next_gen_asset_status_dto)
        print("The response of AssetSaaSPlatformsApi->update_asset_saas_platform_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetSaaSPlatformsApi->update_asset_saas_platform_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **update_client_next_gen_asset_status_dto** | [**UpdateClientNextGenAssetStatusDto**](UpdateClientNextGenAssetStatusDto.md)|  | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

