# datahub_client.ElementApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_element**](ElementApi.md#add_element) | **POST** /elements/{userId}/{dataSet}/{release} | Create a new open element
[**delete_element**](ElementApi.md#delete_element) | **DELETE** /elements/{userId}/{dataSet}/{release}/{element} | Delete element information
[**get_element**](ElementApi.md#get_element) | **GET** /elements/{userId}/{dataSet}/{release}/{element} | Get element information
[**update_element**](ElementApi.md#update_element) | **PUT** /elements/{userId}/{dataSet}/{release}/{element} | Updates an element


# **add_element**
> GeneralStatus add_element(user_id, data_set, release, body, api_key=api_key)

Create a new open element

This creates a new element in a release in a data set. The element defaults to the open (and therefore unpublished) state. 

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.ElementApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release this element belongs to
body = datahub_client.DataElement() # DataElement | Element object that defines the element in a data set
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Create a new open element
    api_response = api_instance.add_element(user_id, data_set, release, body, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ElementApi->add_element: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release this element belongs to | 
 **body** | [**DataElement**](DataElement.md)| Element object that defines the element in a data set | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**GeneralStatus**](GeneralStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_element**
> GeneralStatus delete_element(user_id, data_set, release, element, api_key=api_key)

Delete element information

This removes an element 

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.ElementApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release
element = 'element_example' # str | The id of the element
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Delete element information
    api_response = api_instance.delete_element(user_id, data_set, release, element, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ElementApi->delete_element: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release | 
 **element** | **str**| The id of the element | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**GeneralStatus**](GeneralStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> DataElement get_element(user_id, data_set, release, element, api_key=api_key)

Get element information

This returns information about an element 

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.ElementApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release
element = 'element_example' # str | The id of the element
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Get element information
    api_response = api_instance.get_element(user_id, data_set, release, element, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ElementApi->get_element: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release | 
 **element** | **str**| The id of the element | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**DataElement**](DataElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_element**
> DataElement update_element(user_id, data_set, release, element, body, api_key=api_key)

Updates an element

Updates an element

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.ElementApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
data_set = 'data_set_example' # str | The id of the data set
release = 'release_example' # str | The id of the release
element = 'element_example' # str | The id of the element
body = datahub_client.DataElement() # DataElement | The updated element
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Updates an element
    api_response = api_instance.update_element(user_id, data_set, release, element, body, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ElementApi->update_element: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **data_set** | **str**| The id of the data set | 
 **release** | **str**| The id of the release | 
 **element** | **str**| The id of the element | 
 **body** | [**DataElement**](DataElement.md)| The updated element | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**DataElement**](DataElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

