# swagger_client.DataApi

All URIs are relative to *http://localhost:8081/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_csv_data**](DataApi.md#get_csv_data) | **GET** /data/{owner}/{dataset}/{release}/{element}/getCSVBlock | 
[**put_csv_data**](DataApi.md#put_csv_data) | **POST** /data/{owner}/{dataset}/{release}/{element}/csv | 


# **get_csv_data**
> get_csv_data(api_key, owner, dataset, release, element, with_header=with_header, skip=skip, limit=limit)



Returns a block of CSV data

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | The owner of the data element
dataset = 'dataset_example' # str | The name of the data set
release = 'release_example' # str | The name of the release
element = 'element_example' # str | The element name
with_header = true # bool | Whether to include headers (row 0) (optional)
skip = 56 # int | which page to show (optional)
limit = 56 # int | How many records to return (optional)

try: 
    api_instance.get_csv_data(api_key, owner, dataset, release, element, with_header=with_header, skip=skip, limit=limit)
except ApiException as e:
    print "Exception when calling DataApi->get_csv_data: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **owner** | **str**| The owner of the data element | 
 **dataset** | **str**| The name of the data set | 
 **release** | **str**| The name of the release | 
 **element** | **str**| The element name | 
 **with_header** | **bool**| Whether to include headers (row 0) | [optional] 
 **skip** | **int**| which page to show | [optional] 
 **limit** | **int**| How many records to return | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_csv_data**
> put_csv_data(api_key, owner, dataset, release, element, data)



Writes a block of CSV data

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
api_key = 'api_key_example' # str | The user api key
owner = 'owner_example' # str | The owner of the data element
dataset = 'dataset_example' # str | The name of the data set
release = 'release_example' # str | The name of the release
element = 'element_example' # str | The element name
data = 'data_example' # str | The CSV data to write

try: 
    api_instance.put_csv_data(api_key, owner, dataset, release, element, data)
except ApiException as e:
    print "Exception when calling DataApi->put_csv_data: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The user api key | 
 **owner** | **str**| The owner of the data element | 
 **dataset** | **str**| The name of the data set | 
 **release** | **str**| The name of the release | 
 **element** | **str**| The element name | 
 **data** | **str**| The CSV data to write | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

