# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pattern_to_song_map_playlist_add_index_pattern_name_post**](DefaultApi.md#add_pattern_to_song_map_playlist_add_index_pattern_name_post) | **POST** /playlist/add/{index}/{pattern_name} | Add Pattern To Song Map
[**configure_pattern_pattern_pattern_name_patch**](DefaultApi.md#configure_pattern_pattern_pattern_name_patch) | **PATCH** /pattern/{pattern_name} | Configure Pattern
[**configure_plugin_plugin_plugin_name_patch**](DefaultApi.md#configure_plugin_plugin_plugin_name_patch) | **PATCH** /plugin/{plugin_name} | Configure Plugin
[**create_pattern_pattern_post**](DefaultApi.md#create_pattern_pattern_post) | **POST** /pattern | Create Pattern
[**create_playlist_playlist_post**](DefaultApi.md#create_playlist_playlist_post) | **POST** /playlist | Create Playlist
[**get_pattern_by_name_pattern_pattern_name_get**](DefaultApi.md#get_pattern_by_name_pattern_pattern_name_get) | **GET** /pattern/{pattern_name} | Get Pattern By Name
[**get_playlist_daw_get**](DefaultApi.md#get_playlist_daw_get) | **GET** /daw | Get Playlist
[**get_plugin_by_name_plugin_plugin_name_get**](DefaultApi.md#get_plugin_by_name_plugin_plugin_name_get) | **GET** /plugin/{plugin_name} | Get Plugin By Name
[**get_plugins_plugin_get**](DefaultApi.md#get_plugins_plugin_get) | **GET** /plugin | Get Plugins
[**register_plugin_plugin_post**](DefaultApi.md#register_plugin_plugin_post) | **POST** /plugin | Register Plugin
[**render_playlist_daw_render_get**](DefaultApi.md#render_playlist_daw_render_get) | **GET** /daw/render | Render Playlist
[**save_playlist_daw_save_get**](DefaultApi.md#save_playlist_daw_save_get) | **GET** /daw/save | save playlist
[**update_pattern_pattern_pattern_name_put**](DefaultApi.md#update_pattern_pattern_pattern_name_put) | **PUT** /pattern/{pattern_name} | Update Pattern

# **add_pattern_to_song_map_playlist_add_index_pattern_name_post**
> Pattern add_pattern_to_song_map_playlist_add_index_pattern_name_post(pattern_name, index)

Add Pattern To Song Map

add pattern to songmap at index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
pattern_name = 'pattern_name_example' # str | 
index = 56 # int | 

try:
    # Add Pattern To Song Map
    api_response = api_instance.add_pattern_to_song_map_playlist_add_index_pattern_name_post(pattern_name, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_pattern_to_song_map_playlist_add_index_pattern_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_name** | **str**|  | 
 **index** | **int**|  | 

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_pattern_pattern_pattern_name_patch**
> Object configure_pattern_pattern_pattern_name_patch(pattern_name)

Configure Pattern

Configure Pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
pattern_name = 'pattern_name_example' # str | 

try:
    # Configure Pattern
    api_response = api_instance.configure_pattern_pattern_pattern_name_patch(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->configure_pattern_pattern_pattern_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_name** | **str**|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_plugin_plugin_plugin_name_patch**
> Object configure_plugin_plugin_plugin_name_patch(plugin_name)

Configure Plugin

Configure Plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
plugin_name = 'plugin_name_example' # str | 

try:
    # Configure Plugin
    api_response = api_instance.configure_plugin_plugin_plugin_name_patch(plugin_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->configure_plugin_plugin_plugin_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pattern_pattern_post**
> Object create_pattern_pattern_post(body)

Create Pattern

create a new pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Pattern() # Pattern | 

try:
    # Create Pattern
    api_response = api_instance.create_pattern_pattern_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_pattern_pattern_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pattern**](Pattern.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_playlist_playlist_post**
> Object create_playlist_playlist_post(body)

Create Playlist

create a new playlist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Playlist() # Playlist | 

try:
    # Create Playlist
    api_response = api_instance.create_playlist_playlist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_playlist_playlist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Playlist**](Playlist.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pattern_by_name_pattern_pattern_name_get**
> Pattern get_pattern_by_name_pattern_pattern_name_get(pattern_name)

Get Pattern By Name

Get pattern by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
pattern_name = 'pattern_name_example' # str | 

try:
    # Get Pattern By Name
    api_response = api_instance.get_pattern_by_name_pattern_pattern_name_get(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pattern_by_name_pattern_pattern_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_name** | **str**|  | 

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_daw_get**
> Daw get_playlist_daw_get()

Get Playlist

get current playlist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get Playlist
    api_response = api_instance.get_playlist_daw_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_playlist_daw_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Daw**](Daw.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_by_name_plugin_plugin_name_get**
> Plugin get_plugin_by_name_plugin_plugin_name_get(plugin_name)

Get Plugin By Name

Get plugin by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
plugin_name = 'plugin_name_example' # str | 

try:
    # Get Plugin By Name
    api_response = api_instance.get_plugin_by_name_plugin_plugin_name_get(plugin_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugin_by_name_plugin_plugin_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_plugin_get**
> list[Plugin] get_plugins_plugin_get()

Get Plugins

get registered plugins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get Plugins
    api_response = api_instance.get_plugins_plugin_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugins_plugin_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Plugin]**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_plugin_plugin_post**
> Daw register_plugin_plugin_post(body)

Register Plugin

register a new plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Plugin() # Plugin | 

try:
    # Register Plugin
    api_response = api_instance.register_plugin_plugin_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_plugin_plugin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Plugin**](Plugin.md)|  | 

### Return type

[**Daw**](Daw.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_playlist_daw_render_get**
> str render_playlist_daw_render_get()

Render Playlist

render current playlist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Render Playlist
    api_response = api_instance.render_playlist_daw_render_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->render_playlist_daw_render_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_playlist_daw_save_get**
> str save_playlist_daw_save_get()

save playlist

save current playlist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # save playlist
    api_response = api_instance.save_playlist_daw_save_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_playlist_daw_save_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pattern_pattern_pattern_name_put**
> Pattern update_pattern_pattern_pattern_name_put(pattern_name)

Update Pattern

update a pattern by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
pattern_name = 'pattern_name_example' # str | 

try:
    # Update Pattern
    api_response = api_instance.update_pattern_pattern_pattern_name_put(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_pattern_pattern_pattern_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_name** | **str**|  | 

### Return type

[**Pattern**](Pattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

