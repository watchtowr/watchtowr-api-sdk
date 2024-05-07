# watchtowr_api.ActivityLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_activity_logs**](ActivityLogApi.md#get_list_activity_logs) | **GET** /api/client/activity-log/list | List all activity logs.


# **get_list_activity_logs**
> PaginatedClientActivityLog get_list_activity_logs(page=page, page_size=page_size, created_from=created_from, created_to=created_to, types=types, search=search, user_ids=user_ids)

List all activity logs.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.paginated_client_activity_log import PaginatedClientActivityLog
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
    api_instance = watchtowr_api.ActivityLogApi(api_client)
    page = 1 # float | Pagination page. The default value is 1 (optional)
    page_size = 10 # float | Pagination size. The default value is 10 and the maximum is 30 (optional)
    created_from = '2022-02-22 22:00:00' # datetime | Start Date (optional)
    created_to = '2022-02-23 22:00:00' # datetime | End Date (optional)
    types = ['UserInvite,UserRole,UserLock,ResetUser2FA,SetupSSO,UpdateUserSessionTimeout,SuccessfulLogin,PasswordResetTriggered,IntegrationSetUp,IntegrationUpdated,KillSwitch,FindingSetting,TestingInfrastructureUpdate,UpdatePriorityPort,ReportGenerated,ReportGenerationRequest,ReportDownloaded'] # List[str] | Subject types (optional)
    search = 'e.g access' # str | Description keyword (optional)
    user_ids = ['1,2,3'] # List[str] | User IDs (optional)

    try:
        # List all activity logs.
        api_response = api_instance.get_list_activity_logs(page=page, page_size=page_size, created_from=created_from, created_to=created_to, types=types, search=search, user_ids=user_ids)
        print("The response of ActivityLogApi->get_list_activity_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityLogApi->get_list_activity_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Pagination page. The default value is 1 | [optional] 
 **page_size** | **float**| Pagination size. The default value is 10 and the maximum is 30 | [optional] 
 **created_from** | **datetime**| Start Date | [optional] 
 **created_to** | **datetime**| End Date | [optional] 
 **types** | [**List[str]**](str.md)| Subject types | [optional] 
 **search** | **str**| Description keyword | [optional] 
 **user_ids** | [**List[str]**](str.md)| User IDs | [optional] 

### Return type

[**PaginatedClientActivityLog**](PaginatedClientActivityLog.md)

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

