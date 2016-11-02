# datahub_client.UserApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UserApi.md#delete_user) | **DELETE** /admin/user/{userId} | 
[**get_user**](UserApi.md#get_user) | **GET** /admin/user/{userId} | 
[**get_user_by_email**](UserApi.md#get_user_by_email) | **GET** /admin/getUserByEmail | 
[**get_user_by_tag**](UserApi.md#get_user_by_tag) | **GET** /admin/getUserByTag | 
[**get_user_by_token**](UserApi.md#get_user_by_token) | **GET** /admin/getUserByToken | 
[**put_user**](UserApi.md#put_user) | **PUT** /admin/user/{userId} | 


# **delete_user**
> delete_user(user_id, admin_key=admin_key, api_key=api_key)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
user_id = 'user_id_example' # str | 
admin_key = 'admin_key_example' # str | The admin user api key (optional)
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    api_instance.delete_user(user_id, admin_key=admin_key, api_key=api_key)
except ApiException as e:
    print "Exception when calling UserApi->delete_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_key** | **str**| The admin user api key | [optional] 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id, admin_key=admin_key, api_key=api_key)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
user_id = 'user_id_example' # str | 
admin_key = 'admin_key_example' # str | The admin user api key (optional)
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    api_response = api_instance.get_user(user_id, admin_key=admin_key, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_key** | **str**| The admin user api key | [optional] 
 **api_key** | **str**| The user api key | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_email**
> User get_user_by_email(admin_key, email)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
admin_key = 'admin_key_example' # str | The admin user api key
email = 'email_example' # str | The email to search for

try: 
    api_response = api_instance.get_user_by_email(admin_key, email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user_by_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin user api key | 
 **email** | **str**| The email to search for | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_tag**
> User get_user_by_tag(admin_key, tag_name, tag_value)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
admin_key = 'admin_key_example' # str | The admin user api key
tag_name = 'tag_name_example' # str | The tag field to search (e.g. github)
tag_value = 'tag_value_example' # str | The tag value to search

try: 
    api_response = api_instance.get_user_by_tag(admin_key, tag_name, tag_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user_by_tag: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin user api key | 
 **tag_name** | **str**| The tag field to search (e.g. github) | 
 **tag_value** | **str**| The tag value to search | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_token**
> User get_user_by_token(admin_key, token, expiry)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
admin_key = 'admin_key_example' # str | The admin user api key
token = 'token_example' # str | The token passed by an email
expiry = '2013-10-20' # date | The latest date for which the token is valid

try: 
    api_response = api_instance.get_user_by_token(admin_key, token, expiry)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user_by_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin user api key | 
 **token** | **str**| The token passed by an email | 
 **expiry** | **date**| The latest date for which the token is valid | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user**
> put_user(user_id, body, api_key=api_key)



### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.UserApi()
user_id = 'user_id_example' # str | 
body = datahub_client.User() # User | 
api_key = 'api_key_example' # str | The user api key (optional)

try: 
    api_instance.put_user(user_id, body, api_key=api_key)
except ApiException as e:
    print "Exception when calling UserApi->put_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**User**](User.md)|  | 
 **api_key** | **str**| The user api key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

