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
    print("Exception when calling DefaultApi->getPlaylistDawGet: %s\n" % e)

