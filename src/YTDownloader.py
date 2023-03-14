from pytube import YouTube, exceptions
from sys import argv
import os
import requests

if not os.path.isdir('./src/tmp'):
  os.mkdir('./src/tmp')

call_obj = argv[1]
yt = YouTube(call_obj)
title = yt.title

def download_vid():
  """
  download thumbnail
  """
  try:
    yt.check_availability()
    print(f'downloading {title}...')
    yt.streams.first().download('src/Downloads',f'{title}.mp3',)
    print(f'{title} - download complete')
  except exceptions.VideoUnavailable:
      print(f'{yt} not available - skipping...')
  except KeyError:
    print(f'{yt} error - skipping...')
  except Exception as e:
    print('ERROR:', e)

# def thumbnail_download():
#   """
#   download thumbnail
#   """
  
#   with open(f'./src/tmp/{title}.jpg', 'wb') as handle:
#     response = requests.get(yt.thumbnail_url, stream=True)

#     if not response.ok:
#         print(response)

#     for block in response.iter_content(1024):
#         if not block:
#             break

#         handle.write(block)
  
download_vid()
# thumbnail_download()