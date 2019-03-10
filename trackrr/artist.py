
from .error import *
import requests

class ArtistSearch:

    def __init__(self, search_query, api_key=None):

        if api_key == None:
            raise TrackrrAPIError("API Key is required for artist searches.")
        else:
            pass
        
        self.api_key = api_key
        self.search_query = str(search_query)

        def _params():
            params = {
                'name': self.search_query,
                'key': self.api_key
            }

            return params
        
        def _url():
            return "https://api.trackrr.cc/artist"
        
        def _search_artist():
            try:
                request = requests.get(self.url, params=self.params)
            except Exception as error:
                logger.exception(error)
            
            if request.status_code != 200:
                try:
                    json_parse = request.json()
                    raise TrackrrAPIError(json_parse['message'])
                except Exception:
                    raise TrackrrAPIError(f"{request.status_code} response returned.")
            
            else:
                return request.json()

        self.params = _params()
        self.url = _url()
        self.artist = _search_artist()