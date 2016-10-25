# mimir_client.ReleaseApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_release**](ReleaseApi.md#add_release) | **POST** /releases/{userId}/{dataSet} | Create a new open release
[**delete_release**](ReleaseApi.md#delete_release) | **DELETE** /releases/{userId}/{dataSet}/{release} | Get release information
[**get_release**](ReleaseApi.md#get_release) | **GET** /releases/{userId}/{dataSet}/{release} | Get release information


# **add_release**
> add_release(user_id, data_set, body, api_key=api_key)

Create a new open release

This creates a new release in a data set. The release defaults to the open (and therefore unpublished) state. 

### Example 
```python
import time
import mimir_client
from mimir_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mimir_client.ReleaseApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
body = mimir_client.DataSetRelease() # DataSetRelease | Release object that defines the element in a data set
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Create a new open release
    api_instance.add_release(user_id, data_set, body, api_key=api_key)
except ApiException as e:
    print "Exception when calling ReleaseApi->add_release: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **body** | [**DataSetRelease**](DataSetRelease.md)| Release object that defines the element in a data set | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_release**
> delete_release(user_id, data_set, release, api_key=api_key)

Get release information

This returns information about a release 

### Example 
```python
import time
import mimir_client
from mimir_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mimir_client.ReleaseApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Get release information
    api_instance.delete_release(user_id, data_set, release, api_key=api_key)
except ApiException as e:
    print "Exception when calling ReleaseApi->delete_release: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release**
> DataSetRelease get_release(user_id, data_set, release, api_key=api_key)

Get release information

This returns information about a release 

### Example 
```python
import time
import mimir_client
from mimir_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mimir_client.ReleaseApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Get release information
    api_response = api_instance.get_release(user_id, data_set, release, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReleaseApi->get_release: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**DataSetRelease**](DataSetRelease.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

