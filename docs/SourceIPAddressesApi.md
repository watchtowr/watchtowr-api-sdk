# watchtowr_api.SourceIPAddressesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_source_ip_addresses**](SourceIPAddressesApi.md#get_list_source_ip_addresses) | **GET** /api/client/testing-infrastructure | List all source IP Addresses.


# **get_list_source_ip_addresses**
> ClientSourceIpsAddresses get_list_source_ip_addresses()

List all source IP Addresses.

### Example

* Bearer (Hex string) Authentication (bearer):

```python
import watchtowr_api
from watchtowr_api.models.client_source_ips_addresses import ClientSourceIpsAddresses
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
    api_instance = watchtowr_api.SourceIPAddressesApi(api_client)

    try:
        # List all source IP Addresses.
        api_response = api_instance.get_list_source_ip_addresses()
        print("The response of SourceIPAddressesApi->get_list_source_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceIPAddressesApi->get_list_source_ip_addresses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientSourceIpsAddresses**](ClientSourceIpsAddresses.md)

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

