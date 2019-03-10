
from .error import *
import requests


class SongSearch:

    def __init__(self, search_query, service, api_key=None):

        if api_key == None and service != "spotify":
            raise TrackrrAPIError("API key is required for non-spotify searches.")
        else:
            pass

        self.api_key = api_key
        self.service = service

        self.search_query = str(search_query)

        def _params():

            params = {
                'name': self.search_query,
                'service': self.service,
            }
            if api_key == None:
                pass
            else:
                params['key'] = self.api_key
            return params

        def _url():
            return 'https://api.trackrr.cc/song'



        def _search_song():
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
        self.song = _search_song()