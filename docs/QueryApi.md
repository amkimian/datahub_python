# datahub_client.QueryApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_data**](QueryApi.md#query_data) | **GET** /query/{owner}/{dataset}/{release}/{element} | 


# **query_data**
> str query_data(api_key, owner, dataset, release, element, query, page=page, limit=limit)



Querys data in a KV element

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.QueryApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | 
dataset = 'dataset_example' # str | 
release = 'release_example' # str | 
element = 'element_example' # str | 
query = 'query_example' # str | The query, currently a string rep of a JSON mongo query
page = 56 # int | The page of data to return (optional)
limit = 56 # int | The maximum rows to return (optional)

try: 
    api_response = api_instance.query_data(api_key, owner, dataset, release, element, query, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query_data: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **owner** | **str**|  | 
 **dataset** | **str**|  | 
 **release** | **str**|  | 
 **element** | **str**|  | 
 **query** | **str**| The query, currently a string rep of a JSON mongo query | 
 **page** | **int**| The page of data to return | [optional] 
 **limit** | **int**| The maximum rows to return | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

