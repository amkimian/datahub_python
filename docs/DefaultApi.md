# mimir_client.DefaultApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription_to_invoice**](DefaultApi.md#add_subscription_to_invoice) | **GET** /invoice/addSubscription/{owner}/{dataset} | 


# **add_subscription_to_invoice**
> Invoice add_subscription_to_invoice(api_key, owner, dataset)



Adds the subscription to the current users current invoice

### Example 
```python
import time
import mimir_client
from mimir_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mimir_client.DefaultApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | The owner of the data element
dataset = 'dataset_example' # str | The name of the data set

try: 
    api_response = api_instance.add_subscription_to_invoice(api_key, owner, dataset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->add_subscription_to_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **owner** | **str**| The owner of the data element | 
 **dataset** | **str**| The name of the data set | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

