from pytube import Playlist, exceptions
from sys import argv
import os


call_obj = argv[1]
p = Playlist(call_obj)
playlist_title = p.title

if not os.path.isdir(f'./src/Downloads/{playlist_title}'):
  os.mkdir(f'./src/Downloads/{playlist_title}')

def download_playlist():
  """
  download playlist
  """
  for yt in p.videos:
    try:
      yt.check_availability()
      title = yt.title
    
      print(f'downloading {title}...')
      yt.streams.first().download(f'src/Downloads/{playlist_title}',f'{title}.mp3',)
      print(f'{title} - download complete')
  
    except exceptions.VideoUnavailable:
      print(f'{yt} not available - skipping...')
    except KeyError:
      print(f'{yt} error - skipping...')
    except Exception as e:
      print('ERROR:', e)
    
download_playlist()
