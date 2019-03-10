# Trackrr-Wrapprr


A barebones API wrapper around the [Trackrr API](https://github.com/exofeel/Trackrr-API).


# Install

Coming soon

# Usage

## Song Search


```python
>>> import trackrr

>>> song_query = trackrr.SongSearch('Reborn', 'spotify').song
>>> song_query
{'name': 'Reborn', 'track_album': 'KIDS SEE GHOSTS', 'artist': 'KIDS SEE GHOSTS', 'link': 'https://open.spotify.com/track/4RVbK6cV0VqWdpCDcx3hiT', 'cover_url': 'https://i.scdn.co/image/64cc5671890ba19c6c42a533eed08da56d29bdca', 'service': 'Spotify', 'release_date': 'June 8, 2018', 'status': 'ok'}
>>> song_query['track_album']
'KIDS SEE GHOSTS'
>>> 
```


## Album Search

```python

>> import trackrr

>>> api_key = "d912b6a6-b4b6-43a1-b9ff-2f3f7203ad24"

>>> album_search = trackrr.AlbumSearch('The Life Of Pablo', 'tidal', api_key).album

>>> album_search
{'name': 'The Life Of Pablo', 'track_list': ['Ultralight Beam', 'Father Stretch My Hands Pt. 1', 'Pt. 2', 'Famous', 'Feedback', 'Low Lights', 'Highlights', 'Freestyle 4', 'I Love Kanye', 'Waves', 'FML', 'Real Friends', 'Wolves', "Frank's Track", 'Siiiiiiiiilver Surffffeeeeer Intermission', '30 Hours', 'No More Parties In LA', 'Facts (Charlie Heat Version)', 'Fade', 'Saint Pablo'], 'artist': 'Kanye West', 'link': 'http://www.tidal.com/album/57273408', 'cover_url': 'https://resources.wimpmusic.com/images/114d07f0/0070/4a98/b7e8/0b4f77ce47cd/1280x1280.jpg', 'service': 'Tidal', 'release_date': 'June 10, 2016', 'status': 'ok'}

>>> album_search['artist']
'Kanye West'

>>> 
```


# Exceptions

- ``trackrr.error.TrackrrAPI``
- ``trackrr.error.SongNotFound``
- ``trackrr.error.AlbumNotFound``


# Requirements

- requests

