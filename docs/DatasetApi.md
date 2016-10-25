# swagger_client.DatasetApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_set**](DatasetApi.md#add_data_set) | **POST** /datasets/{userId} | Create a new data set, associated with the given user id
[**delete_data_set**](DatasetApi.md#delete_data_set) | **DELETE** /datasets/{userId}/{dataSet} | Remove a data set and all releases and elements
[**find_data_sets_by_tags**](DatasetApi.md#find_data_sets_by_tags) | **GET** /marketplace/getByTag | 
[**find_user_data_sets**](DatasetApi.md#find_user_data_sets) | **GET** /user/getDataSets | 
[**get_data_set_by_id**](DatasetApi.md#get_data_set_by_id) | **GET** /datasets/{userId}/{dataSet} | Find a dataset for a user and a dataset
[**get_front**](DatasetApi.md#get_front) | **GET** /marketplace/getFront | 
[**get_my_data_sets**](DatasetApi.md#get_my_data_sets) | **GET** /marketplace/getMyDataSets | 
[**update_data_set**](DatasetApi.md#update_data_set) | **PUT** /datasets/{userId}/{dataSet} | Update an existing data set.


# **add_data_set**
> add_data_set(user_id, body, api_key=api_key)

Create a new data set, associated with the given user id

This creates a new data set that can then be added to 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
user_id = 'user_id_example' # str | The id of the user that this dataset is associated with
body = swagger_client.DataSet() # DataSet | DataSet object that defines the element
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Create a new data set, associated with the given user id
    api_instance.add_data_set(user_id, body, api_key=api_key)
except ApiException as e:
    print "Exception when calling DatasetApi->add_data_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user that this dataset is associated with | 
 **body** | [**DataSet**](DataSet.md)| DataSet object that defines the element | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_set**
> delete_data_set(user_id, data_set, api_key=api_key)

Remove a data set and all releases and elements



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
user_id = 'user_id_example' # str | The id of the user owning this dataset
data_set = 'data_set_example' # str | The id of the dataset
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Remove a data set and all releases and elements
    api_instance.delete_data_set(user_id, data_set, api_key=api_key)
except ApiException as e:
    print "Exception when calling DatasetApi->delete_data_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user owning this dataset | 
 **data_set** | **str**| The id of the dataset | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_data_sets_by_tags**
> list[DataSet] find_data_sets_by_tags(api_key=api_key, tags=tags, page=page)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
api_key = 'api_key_example' # str | The user api key (optional)
tags = ['tags_example'] # list[str] | Tags to filter by (optional)
page = 56 # int | Page to return (defaults to zero) (optional)

try: 
    api_response = api_instance.find_data_sets_by_tags(api_key=api_key, tags=tags, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DatasetApi->find_data_sets_by_tags: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | [optional] 
 **tags** | [**list[str]**](str.md)| Tags to filter by | [optional] 
 **page** | **int**| Page to return (defaults to zero) | [optional] 

### Return type

[**list[DataSet]**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_data_sets**
> list[DataSet] find_user_data_sets(api_key, tags=tags, page=page, subscribed=subscribed)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
api_key = 'api_key_example' # str | The user api key
tags = ['tags_example'] # list[str] | Tags to filter by (optional)
page = 56 # int | Page to return (defaults to zero) (optional)
subscribed = true # bool | If true, also return subscribed data sets (optional)

try: 
    api_response = api_instance.find_user_data_sets(api_key, tags=tags, page=page, subscribed=subscribed)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DatasetApi->find_user_data_sets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **tags** | [**list[str]**](str.md)| Tags to filter by | [optional] 
 **page** | **int**| Page to return (defaults to zero) | [optional] 
 **subscribed** | **bool**| If true, also return subscribed data sets | [optional] 

### Return type

[**list[DataSet]**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_by_id**
> DataSet get_data_set_by_id(user_id, data_set, api_key=api_key)

Find a dataset for a user and a dataset

Returns a data set

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
user_id = 'user_id_example' # str | The id of the user owning this dataset
data_set = 'data_set_example' # str | The id of the dataset
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    # Find a dataset for a user and a dataset
    api_response = api_instance.get_data_set_by_id(user_id, data_set, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DatasetApi->get_data_set_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user owning this dataset | 
 **data_set** | **str**| The id of the dataset | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**DataSet**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_front**
> list[DataSet] get_front(page=page, limit=limit)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
page = 56 # int | Page to return (defaults to zero) (optional)
limit = 56 # int | The maximum amount of records to be returned (the size of the page) (optional)

try: 
    api_response = api_instance.get_front(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DatasetApi->get_front: %s\n" % e
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

# **get_my_data_sets**
> list[DataSet] get_my_data_sets(api_key, page=page)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
api_key = 'api_key_example' # str | The user api key
page = 56 # int | Page to return (defaults to zero) (optional)

try: 
    api_response = api_instance.get_my_data_sets(api_key, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DatasetApi->get_my_data_sets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **page** | **int**| Page to return (defaults to zero) | [optional] 

### Return type

[**list[DataSet]**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_set**
> update_data_set(api_key, owner, dataset, body)

Update an existing data set.



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatasetApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | The id of the user that this dataset is associated with
dataset = 'dataset_example' # str | The data set id to update
body = swagger_client.DataSet() # DataSet | DataSet object that defines the element

try: 
    # Update an existing data set.
    api_instance.update_data_set(api_key, owner, dataset, body)
except ApiException as e:
    print "Exception when calling DatasetApi->update_data_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **owner** | **str**| The id of the user that this dataset is associated with | 
 **dataset** | **str**| The data set id to update | 
 **body** | [**DataSet**](DataSet.md)| DataSet object that defines the element | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

