import io
import re
import urllib.request

def getUrl(file, folder):
    aurl = input('링크를 적어주세요 \n')

    urllib.request.urlretrieve(aurl, f"./{folder}/{}audio.mp4")
