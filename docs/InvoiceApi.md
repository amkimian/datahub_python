# datahub_client.InvoiceApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription_to_invoice**](InvoiceApi.md#add_subscription_to_invoice) | **GET** /invoice/addSubscription/{owner}/{dataset} | 
[**get_cart**](InvoiceApi.md#get_cart) | **GET** /invoice/retrieveCurrent | 
[**get_invoices**](InvoiceApi.md#get_invoices) | **GET** /invoice/retrieve | 
[**process_cart**](InvoiceApi.md#process_cart) | **GET** /invoice/processCurrent | 


# **add_subscription_to_invoice**
> Invoice add_subscription_to_invoice(api_key, owner, dataset)



Adds the subscription to the current users current invoice

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.InvoiceApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | The owner of the data element
dataset = 'dataset_example' # str | The name of the data set

try: 
    api_response = api_instance.add_subscription_to_invoice(api_key, owner, dataset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoiceApi->add_subscription_to_invoice: %s\n" % e
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

# **get_cart**
> Invoice get_cart(api_key)



retrieve the current open oneoff invoice

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.InvoiceApi()
api_key = 'api_key_example' # str | The user api key

try: 
    api_response = api_instance.get_cart(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoiceApi->get_cart: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> list[Invoice] get_invoices(api_key, page=page)



retrieve a page of invoices

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.InvoiceApi()
api_key = 'api_key_example' # str | The user api key
page = 56 # int | The page to show (optional)

try: 
    api_response = api_instance.get_invoices(api_key, page=page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoiceApi->get_invoices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **page** | **int**| The page to show | [optional] 

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_cart**
> Invoice process_cart(api_key)



Process a successful payment

### Example 
```python
import time
import datahub_client
from datahub_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = datahub_client.InvoiceApi()
api_key = 'api_key_example' # str | The user api key

try: 
    api_response = api_instance.process_cart(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoiceApi->process_cart: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

