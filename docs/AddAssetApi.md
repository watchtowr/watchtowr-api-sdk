# watchtowr_api.AddAssetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_asset**](AddAssetApi.md#submit_asset) | **POST** /api/client/seeddata | Add asset to your attack surface for review.


# **submit_asset**
> ClientSeedDataData submit_asset(create_client_seed_data_request_body)

Add asset to your attack surface for review.

### Example

* Bearer (Hex string) Authentication (bearer):
```python
import time
import os
import watchtowr_api
from watchtowr_api.models.client_seed_data_data import ClientSeedDataData
from watchtowr_api.models.create_client_seed_data_request_body import CreateClientSeedDataRequestBody
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
    api_instance = watchtowr_api.AddAssetApi(api_client)
    create_client_seed_data_request_body = watchtowr_api.CreateClientSeedDataRequestBody() # CreateClientSeedDataRequestBody | 

    try:
        # Add asset to your attack surface for review.
        api_response = api_instance.submit_asset(create_client_seed_data_request_body)
        print("The response of AddAssetApi->submit_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddAssetApi->submit_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_seed_data_request_body** | [**CreateClientSeedDataRequestBody**](CreateClientSeedDataRequestBody.md)|  | 

### Return type

[**ClientSeedDataData**](ClientSeedDataData.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

