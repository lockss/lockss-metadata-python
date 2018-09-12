# lockss_metadata.UrlsApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_urls_doi**](UrlsApi.md#get_urls_doi) | **GET** /urls/doi | Gets the URL for a DOI
[**get_urls_open_url**](UrlsApi.md#get_urls_open_url) | **GET** /urls/openurl | Performs an OpenURL query


# **get_urls_doi**
> UrlInfo get_urls_doi(doi)

Gets the URL for a DOI

Provides the URL for a DOI given the DOI

### Example
```python
from __future__ import print_function
import time
import lockss_metadata
from lockss_metadata.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_metadata.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_metadata.UrlsApi(lockss_metadata.ApiClient(configuration))
doi = 'doi_example' # str | The DOI for which the URL is requested

try:
    # Gets the URL for a DOI
    api_response = api_instance.get_urls_doi(doi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlsApi->get_urls_doi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi** | **str**| The DOI for which the URL is requested | 

### Return type

[**UrlInfo**](UrlInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_urls_open_url**
> UrlInfo get_urls_open_url(params)

Performs an OpenURL query

Provides the URL that results from performing an OpenURL query. With query parameters inline

### Example
```python
from __future__ import print_function
import time
import lockss_metadata
from lockss_metadata.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_metadata.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_metadata.UrlsApi(lockss_metadata.ApiClient(configuration))
params = ['params_example'] # list[str] | The OpenURL parameters

try:
    # Performs an OpenURL query
    api_response = api_instance.get_urls_open_url(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlsApi->get_urls_open_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**list[str]**](str.md)| The OpenURL parameters | 

### Return type

[**UrlInfo**](UrlInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

