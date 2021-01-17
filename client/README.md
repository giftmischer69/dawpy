# swagger-client
This is the daw server api

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

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
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pattern_name = 'pattern_name_example' # str | 
index = 56 # int | 

try:
    # Add Pattern To Song Map
    api_response = api_instance.add_pattern_to_song_map_playlist_add_index_pattern_name_post(pattern_name, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_pattern_to_song_map_playlist_add_index_pattern_name_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pattern_name = 'pattern_name_example' # str | 

try:
    # Configure Pattern
    api_response = api_instance.configure_pattern_pattern_pattern_name_patch(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->configure_pattern_pattern_pattern_name_patch: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 

try:
    # Configure Plugin
    api_response = api_instance.configure_plugin_plugin_plugin_name_patch(plugin_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->configure_plugin_plugin_plugin_name_patch: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pattern() # Pattern | 

try:
    # Create Pattern
    api_response = api_instance.create_pattern_pattern_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_pattern_pattern_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Playlist() # Playlist | 

try:
    # Create Playlist
    api_response = api_instance.create_playlist_playlist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_playlist_playlist_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pattern_name = 'pattern_name_example' # str | 

try:
    # Get Pattern By Name
    api_response = api_instance.get_pattern_by_name_pattern_pattern_name_get(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pattern_by_name_pattern_pattern_name_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Playlist
    api_response = api_instance.get_playlist_daw_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_playlist_daw_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 

try:
    # Get Plugin By Name
    api_response = api_instance.get_plugin_by_name_plugin_plugin_name_get(plugin_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugin_by_name_plugin_plugin_name_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Plugins
    api_response = api_instance.get_plugins_plugin_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugins_plugin_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Plugin() # Plugin | 

try:
    # Register Plugin
    api_response = api_instance.register_plugin_plugin_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_plugin_plugin_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Render Playlist
    api_response = api_instance.render_playlist_daw_render_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->render_playlist_daw_render_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # save playlist
    api_response = api_instance.save_playlist_daw_save_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_playlist_daw_save_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pattern_name = 'pattern_name_example' # str | 

try:
    # Update Pattern
    api_response = api_instance.update_pattern_pattern_pattern_name_put(pattern_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_pattern_pattern_pattern_name_put: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_pattern_to_song_map_playlist_add_index_pattern_name_post**](docs/DefaultApi.md#add_pattern_to_song_map_playlist_add_index_pattern_name_post) | **POST** /playlist/add/{index}/{pattern_name} | Add Pattern To Song Map
*DefaultApi* | [**configure_pattern_pattern_pattern_name_patch**](docs/DefaultApi.md#configure_pattern_pattern_pattern_name_patch) | **PATCH** /pattern/{pattern_name} | Configure Pattern
*DefaultApi* | [**configure_plugin_plugin_plugin_name_patch**](docs/DefaultApi.md#configure_plugin_plugin_plugin_name_patch) | **PATCH** /plugin/{plugin_name} | Configure Plugin
*DefaultApi* | [**create_pattern_pattern_post**](docs/DefaultApi.md#create_pattern_pattern_post) | **POST** /pattern | Create Pattern
*DefaultApi* | [**create_playlist_playlist_post**](docs/DefaultApi.md#create_playlist_playlist_post) | **POST** /playlist | Create Playlist
*DefaultApi* | [**get_pattern_by_name_pattern_pattern_name_get**](docs/DefaultApi.md#get_pattern_by_name_pattern_pattern_name_get) | **GET** /pattern/{pattern_name} | Get Pattern By Name
*DefaultApi* | [**get_playlist_daw_get**](docs/DefaultApi.md#get_playlist_daw_get) | **GET** /daw | Get Playlist
*DefaultApi* | [**get_plugin_by_name_plugin_plugin_name_get**](docs/DefaultApi.md#get_plugin_by_name_plugin_plugin_name_get) | **GET** /plugin/{plugin_name} | Get Plugin By Name
*DefaultApi* | [**get_plugins_plugin_get**](docs/DefaultApi.md#get_plugins_plugin_get) | **GET** /plugin | Get Plugins
*DefaultApi* | [**register_plugin_plugin_post**](docs/DefaultApi.md#register_plugin_plugin_post) | **POST** /plugin | Register Plugin
*DefaultApi* | [**render_playlist_daw_render_get**](docs/DefaultApi.md#render_playlist_daw_render_get) | **GET** /daw/render | Render Playlist
*DefaultApi* | [**save_playlist_daw_save_get**](docs/DefaultApi.md#save_playlist_daw_save_get) | **GET** /daw/save | save playlist
*DefaultApi* | [**update_pattern_pattern_pattern_name_put**](docs/DefaultApi.md#update_pattern_pattern_pattern_name_put) | **PUT** /pattern/{pattern_name} | Update Pattern

## Documentation For Models

 - [Daw](docs/Daw.md)
 - [DawConfig](docs/DawConfig.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Pattern](docs/Pattern.md)
 - [Playlist](docs/Playlist.md)
 - [Plugin](docs/Plugin.md)
 - [SongMap](docs/SongMap.md)
 - [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

