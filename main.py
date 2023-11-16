import eel
eel.init("web")

from pywnp import WNPRedux


# Start WNP, providing a port, version number and a logger
WNPRedux.start(4500, '1.0.0', print)

eel.start("index.html", block=False, app_mode=True) #400x340 window works best

# Update stuff on interface
def GetInfo():
  song = WNPRedux.media_info.title
  artist = WNPRedux.media_info.artist
  url = WNPRedux.media_info.cover_url
  eel.UpdateData(song, artist, url)
  return (song, artist, url)

def GetPercent():
  percent = WNPRedux.media_info.position_percent
  eel.UpdateProgress(percent)
  return (percent)
  
# Functions for skipping and pausing, called from front end javascript
@eel.expose
def Pause():
  WNPRedux.media_info.controls.try_toggle_play_pause()

@eel.expose
def Skip():
  WNPRedux.media_info.controls.try_skip_next()

@eel.expose
def Previous():
  WNPRedux.media_info.controls.try_skip_previous()


eel.sleep(2)

# Update info every second
while True:
  GetInfo()
  GetPercent()
  eel.sleep(1)