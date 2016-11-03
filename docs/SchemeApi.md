# datahub_client.SchemeApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheme**](SchemeApi.md#create_scheme) | **POST** /scheme/{id} | 
[**delete_scheme**](SchemeApi.md#delete_scheme) | **DELETE** /scheme/{id} | Remove a scheme
[**get_scheme**](SchemeApi.md#get_scheme) | **GET** /scheme/{id} | 
[**get_schemes**](SchemeApi.md#get_schemes) | **GET** /schemes/get | 
[**update_scheme**](SchemeApi.md#update_scheme) | **PUT** /scheme/{id} | Update an existing scheme.


# **create_scheme**
> GeneralStatus create_scheme(admin_key, id, body)



Create a scheme

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.SchemeApi()
admin_key = 'admin_key_example' # str | The admin api key
id = 'id_example' # str | The id of the scheme
body = datahub_client.Scheme() # Scheme | DataSet object that defines the element

try: 
    api_response = api_instance.create_scheme(admin_key, id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchemeApi->create_scheme: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin api key | 
 **id** | **str**| The id of the scheme | 
 **body** | [**Scheme**](Scheme.md)| DataSet object that defines the element | 

### Return type

[**GeneralStatus**](GeneralStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheme**
> GeneralStatus delete_scheme(admin_key, id)

Remove a scheme



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.SchemeApi()
admin_key = 'admin_key_example' # str | The admin key
id = 'id_example' # str | The id of the scheme

try: 
    # Remove a scheme
    api_response = api_instance.delete_scheme(admin_key, id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchemeApi->delete_scheme: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin key | 
 **id** | **str**| The id of the scheme | 

### Return type

[**GeneralStatus**](GeneralStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheme**
> Scheme get_scheme(api_key, id)



retrieve a scheme

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.SchemeApi()
api_key = 'api_key_example' # str | user api key
id = 'id_example' # str | The id of the scheme

try: 
    api_response = api_instance.get_scheme(api_key, id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchemeApi->get_scheme: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| user api key | 
 **id** | **str**| The id of the scheme | 

### Return type

[**Scheme**](Scheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemes**
> list[Scheme] get_schemes(admin_key, page=page, limit=limit)



Retrieve schemes

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.SchemeApi()
admin_key = 'admin_key_example' # str | The admin api key
page = 56 # int | The page of schemes to return (optional)
limit = 56 # int | The limit of schemes to return (the page size) (optional)

try: 
    api_response = api_instance.get_schemes(admin_key, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchemeApi->get_schemes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin api key | 
 **page** | **int**| The page of schemes to return | [optional] 
 **limit** | **int**| The limit of schemes to return (the page size) | [optional] 

### Return type

[**list[Scheme]**](Scheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheme**
> GeneralStatus update_scheme(api_key, id, body)

Update an existing scheme.

Update scheme

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.SchemeApi()
api_key = 'api_key_example' # str | The user api key
id = 'id_example' # str | The id of the scheme
body = datahub_client.Scheme() # Scheme | Scheme object that defines the element

try: 
    # Update an existing scheme.
    api_response = api_instance.update_scheme(api_key, id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchemeApi->update_scheme: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **id** | **str**| The id of the scheme | 
 **body** | [**Scheme**](Scheme.md)| Scheme object that defines the element | 

### Return type

[**GeneralStatus**](GeneralStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

