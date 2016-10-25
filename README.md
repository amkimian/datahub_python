# swagger_client
No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.9
- Package version: 1.0.0
- Build date: 2016-10-25T16:21:23.021-07:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.AdminApi
admin_key = 'admin_key_example' # str | The admin user api key
body = swagger_client.User() # User | A new user

try:
    api_response = api_instance.create_user(admin_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->create_user: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8081/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**create_user**](docs/AdminApi.md#create_user) | **POST** /admin/user | 
*DataApi* | [**get_csv_data**](docs/DataApi.md#get_csv_data) | **GET** /data/{owner}/{dataset}/{release}/{element}/getCSVBlock | 
*DataApi* | [**put_csv_data**](docs/DataApi.md#put_csv_data) | **POST** /data/{owner}/{dataset}/{release}/{element}/csv | 
*DatasetApi* | [**add_data_set**](docs/DatasetApi.md#add_data_set) | **POST** /datasets/{userId} | Create a new data set, associated with the given user id
*DatasetApi* | [**delete_data_set**](docs/DatasetApi.md#delete_data_set) | **DELETE** /datasets/{userId}/{dataSet} | Remove a data set and all releases and elements
*DatasetApi* | [**find_data_sets_by_tags**](docs/DatasetApi.md#find_data_sets_by_tags) | **GET** /marketplace/getByTag | 
*DatasetApi* | [**find_user_data_sets**](docs/DatasetApi.md#find_user_data_sets) | **GET** /user/getDataSets | 
*DatasetApi* | [**get_data_set_by_id**](docs/DatasetApi.md#get_data_set_by_id) | **GET** /datasets/{userId}/{dataSet} | Find a dataset for a user and a dataset
*DatasetApi* | [**get_front**](docs/DatasetApi.md#get_front) | **GET** /marketplace/getFront | 
*DatasetApi* | [**get_my_data_sets**](docs/DatasetApi.md#get_my_data_sets) | **GET** /marketplace/getMyDataSets | 
*DatasetApi* | [**update_data_set**](docs/DatasetApi.md#update_data_set) | **PUT** /datasets/{userId}/{dataSet} | Update an existing data set.
*ElementApi* | [**add_element**](docs/ElementApi.md#add_element) | **POST** /elements/{userId}/{dataSet}/{release} | Create a new open element
*ElementApi* | [**delete_element**](docs/ElementApi.md#delete_element) | **DELETE** /elements/{userId}/{dataSet}/{release}/{element} | Delete element information
*ElementApi* | [**get_element**](docs/ElementApi.md#get_element) | **GET** /elements/{userId}/{dataSet}/{release}/{element} | Get element information
*ElementApi* | [**update_element**](docs/ElementApi.md#update_element) | **PUT** /elements/{userId}/{dataSet}/{release}/{element} | Updates an element
*MarketplaceApi* | [**get_front**](docs/MarketplaceApi.md#get_front) | **GET** /marketplace/getFront | 
*ReleaseApi* | [**add_release**](docs/ReleaseApi.md#add_release) | **POST** /releases/{userId}/{dataSet} | Create a new open release
*ReleaseApi* | [**delete_release**](docs/ReleaseApi.md#delete_release) | **DELETE** /releases/{userId}/{dataSet}/{release} | Get release information
*ReleaseApi* | [**get_release**](docs/ReleaseApi.md#get_release) | **GET** /releases/{userId}/{dataSet}/{release} | Get release information
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /admin/user/{userId} | 
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /admin/user/{userId} | 
*UserApi* | [**get_user_by_email**](docs/UserApi.md#get_user_by_email) | **GET** /admin/getUserByEmail | 
*UserApi* | [**get_user_by_tag**](docs/UserApi.md#get_user_by_tag) | **GET** /admin/getUserByTag | 
*UserApi* | [**get_user_by_token**](docs/UserApi.md#get_user_by_token) | **GET** /admin/getUserByToken | 
*UserApi* | [**put_user**](docs/UserApi.md#put_user) | **PUT** /admin/user/{userId} | 
*ViewApi* | [**get_data_set_releases**](docs/ViewApi.md#get_data_set_releases) | **GET** /view/releases/{userId}/{dataset} | 
*ViewApi* | [**get_release_elements**](docs/ViewApi.md#get_release_elements) | **GET** /view/elements/{userId}/{dataset}/{release} | 
*ViewApi* | [**get_user_views**](docs/ViewApi.md#get_user_views) | **GET** /view/getUserViews | 


## Documentation For Models

 - [DataElement](docs/DataElement.md)
 - [DataElementCsvInfo](docs/DataElementCsvInfo.md)
 - [DataElementDisplayInfo](docs/DataElementDisplayInfo.md)
 - [DataSet](docs/DataSet.md)
 - [DataSetRelease](docs/DataSetRelease.md)
 - [DataSetView](docs/DataSetView.md)
 - [GeneralError](docs/GeneralError.md)
 - [GeneralText](docs/GeneralText.md)
 - [User](docs/User.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserTokens](docs/UserTokens.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## admin_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author



