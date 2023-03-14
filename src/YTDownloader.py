from pytube import YouTube
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
  print(f'downloading {title}...')
  yt.streams.first().download('src/Downloads',f'{title}.mp3',)

  print(f'{title} - download complete')
  
def thumbnail_download():
  """
  download thumbnail
  """
  
  with open(f'./src/tmp/{title}.jpg', 'wb') as handle:
    response = requests.get(yt.thumbnail_url, stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
  
download_vid()
thumbnail_download()