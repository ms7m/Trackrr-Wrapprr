
from .error import *
import requests

class AlbumSearch:
    
    def __init__(self, search_query, service, api_key=None):

        if api_key is None:
            raise TrackrrAPIError("API Key is required for album searches")
        else:
            pass

        self.api_key = api_key
        self.service = service

        self.search_query = str(search_query)

        def _url():
            return 'https://api.trackrr.cc/album'

        def _params():

            params = {
                'name': self.search_query,
                'service': self.service,
                'key': self.api_key
            }
            return params


        def _search_album():

            try:
                request = requests.get(self.url, params=self.params)
            except Exception as error:
                logger.exception(error)

            if request.status_code != 200:
                try:
                    json_parse = request.json()
                    raise TrackrrAPIError(json_parse['message'])
                except Exception as error:
                    raise TrackrrAPIError(f"{request.status_code} response returned.")

            else:
                return request.json()


        self.params = _params()
        self.url = _url()

        self.album = _search_album()