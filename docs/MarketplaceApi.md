# mimir_client.MarketplaceApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_front**](MarketplaceApi.md#get_front) | **GET** /marketplace/getFront | 


# **get_front**
> list[DataSet] get_front(page=page, limit=limit)



### Example 
```python
import time
import mimir_client
from mimir_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mimir_client.MarketplaceApi()
page = 56 # int | Page to return (defaults to zero) (optional)
limit = 56 # int | The maximum amount of records to be returned (the size of the page) (optional)

try: 
    api_response = api_instance.get_front(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MarketplaceApi->get_front: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to return (defaults to zero) | [optional] 
 **limit** | **int**| The maximum amount of records to be returned (the size of the page) | [optional] 

### Return type

[**list[DataSet]**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

