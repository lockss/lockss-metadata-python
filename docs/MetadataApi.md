# lockss_metadata.MetadataApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_aus_auid**](MetadataApi.md#delete_metadata_aus_auid) | **DELETE** /metadata/aus/{auid} | Delete the metadata stored for an AU
[**get_metadata_aus_auid**](MetadataApi.md#get_metadata_aus_auid) | **GET** /metadata/aus/{auid} | Get the metadata stored for an AU
[**post_metadata_aus_item**](MetadataApi.md#post_metadata_aus_item) | **POST** /metadata/aus | Store the metadata for an AU item


# **delete_metadata_aus_auid**
> int delete_metadata_aus_auid(auid)

Delete the metadata stored for an AU

Delete the metadata stored for an AU given the AU identifier

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
api_instance = lockss_metadata.MetadataApi(lockss_metadata.ApiClient(configuration))
auid = 'auid_example' # str | The identifier of the AU for which the metadata is to be deleted

try:
    # Delete the metadata stored for an AU
    api_response = api_instance.delete_metadata_aus_auid(auid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_metadata_aus_auid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auid** | **str**| The identifier of the AU for which the metadata is to be deleted | 

### Return type

**int**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_aus_auid**
> AuMetadataPageInfo get_metadata_aus_auid(auid, limit=limit, continuation_token=continuation_token)

Get the metadata stored for an AU

Get the full metadata stored for an AU given the AU identifier or a pageful of the metadata defined by the continuation token and size

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
api_instance = lockss_metadata.MetadataApi(lockss_metadata.ApiClient(configuration))
auid = 'auid_example' # str | The identifier of the AU for which the metadata is requested
limit = 50 # int | The number of items per page (optional) (default to 50)
continuation_token = 'continuation_token_example' # str | The continuation token of the next page of metadata to be returned (optional)

try:
    # Get the metadata stored for an AU
    api_response = api_instance.get_metadata_aus_auid(auid, limit=limit, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_aus_auid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auid** | **str**| The identifier of the AU for which the metadata is requested | 
 **limit** | **int**| The number of items per page | [optional] [default to 50]
 **continuation_token** | **str**| The continuation token of the next page of metadata to be returned | [optional] 

### Return type

[**AuMetadataPageInfo**](AuMetadataPageInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_metadata_aus_item**
> int post_metadata_aus_item(item)

Store the metadata for an AU item

Store the metadata for an item belonging to an AU

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
api_instance = lockss_metadata.MetadataApi(lockss_metadata.ApiClient(configuration))
item = lockss_metadata.ItemMetadata() # ItemMetadata | The metadata of the AU item to be stored

try:
    # Store the metadata for an AU item
    api_response = api_instance.post_metadata_aus_item(item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->post_metadata_aus_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**ItemMetadata**](ItemMetadata.md)| The metadata of the AU item to be stored | 

### Return type

**int**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

