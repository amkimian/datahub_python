# swagger_client.ViewApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_set_releases**](ViewApi.md#get_data_set_releases) | **GET** /view/releases/{userId}/{dataset} | 
[**get_release_elements**](ViewApi.md#get_release_elements) | **GET** /view/elements/{userId}/{dataset}/{release} | 
[**get_user_views**](ViewApi.md#get_user_views) | **GET** /view/getUserViews | 


# **get_data_set_releases**
> list[DataSetRelease] get_data_set_releases(api_key, user_id, dataset)



Returns releases for a given data set

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewApi()
api_key = 'api_key_example' # str | The user api key
user_id = 'user_id_example' # str | The user id that owns the data set
dataset = 'dataset_example' # str | The id of the data set

try: 
    api_response = api_instance.get_data_set_releases(api_key, user_id, dataset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewApi->get_data_set_releases: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **user_id** | **str**| The user id that owns the data set | 
 **dataset** | **str**| The id of the data set | 

### Return type

[**list[DataSetRelease]**](DataSetRelease.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_elements**
> list[DataElement] get_release_elements(api_key, user_id, dataset, release)



Returns the element information for a given release

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewApi()
api_key = 'api_key_example' # str | The user api key
user_id = 'user_id_example' # str | 
dataset = 'dataset_example' # str | 
release = 'release_example' # str | 

try: 
    api_response = api_instance.get_release_elements(api_key, user_id, dataset, release)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewApi->get_release_elements: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **user_id** | **str**|  | 
 **dataset** | **str**|  | 
 **release** | **str**|  | 

### Return type

[**list[DataElement]**](DataElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_views**
> list[DataSetView] get_user_views(api_key, page=page)



Returns view information for datasets of a user

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewApi()
api_key = 'api_key_example' # str | The user api key
page = 56 # int | The page of results to return (optional)

try: 
    api_response = api_instance.get_user_views(api_key, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewApi->get_user_views: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **page** | **int**| The page of results to return | [optional] 

### Return type

[**list[DataSetView]**](DataSetView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

