from client import swagger_client
from client.swagger_client.rest import ApiException

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get list of exposure types
    api_response = api_instance.get_playlist()
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->exposures_get: %s\n" % e)
