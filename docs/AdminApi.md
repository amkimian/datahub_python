# swagger_client.AdminApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](AdminApi.md#create_user) | **POST** /admin/user | 


# **create_user**
> User create_user(admin_key, body)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
admin_key = 'admin_key_example' # str | The admin user api key
body = swagger_client.User() # User | A new user

try: 
    api_response = api_instance.create_user(admin_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_key** | **str**| The admin user api key | 
 **body** | [**User**](User.md)| A new user | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

