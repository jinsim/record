import io
import os.path
import re
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image

def getUrl(file, folder):
    f = open(file, "r", encoding="UTF8")
    atxt = f.read()
    soup = BeautifulSoup(atxt, 'html.parser')
    title = soup.find("meta", {"property":"og:title"})['content']
    print(title)
    # imus = imurl.split("/slides/")
    # print("----")
    # print(soup)
    # tm = soup.findAll('div',{'class':'vc-chapter-item-time-text-vertical'})
    video_link = soup.select("#video-play-video1 > div.vc-vplay-container.non-selectable > video")[0]['src']
    file_name = f"../{folder}/{title}.mp4"

    if os.path.isfile(file_name):
        print("이미 파일이 존재합니다.")
    else:
        print("MP4 Downloading...",end='')
        urllib.request.urlretrieve(video_link, file_name)
    print('done')
    # tm_text_all = str()
    # i = 0
    # for t in tm:
    #     i += 1
    #     # print(t.text)
    #     tm_text = str()
    #     tm_text = str(i) + "번째 시간" + "\t" + str(t.text) + "\n"
    #     # print(type(tm_text_all))
    #     # print(type(tm_text))
    #     tm_text_all += tm_text
    # # print("----")
    # f = open(f'./{folder}/{th}.txt', 'w', newline='')
    # # print(tm_text_all)
    # f.write(tm_text_all)
    # # print(imus[0])
    # p = re.compile("small_slide_\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\)\.png")
    # res1 = p.findall(atxt)
    # reslen = len(res1)
    # print("Pictures Downloading...")
    # imgs = list()
    # for i in range(0, reslen//2):
    #     tpic = res1[i]
    #     tpic = tpic.replace("small_slide","large_slide")
    #     tpic = tpic.replace(".png",".jpg")
    #     turl = imus[0] + "/slide/" + tpic
    #     urllib.request.urlretrieve(turl,f"./{folder}/{th}"+str(i+1)+".jpg")
    #     print(str(i+1)+"/"+str(reslen//2)+" Complete")
    #     if i == 0:
    #         img1 = Image.open(f"./{folder}/{th}1.jpg")
    #         im1 = img1.convert("RGB")
    #     else:
    #         imgX = Image.open(f"./{folder}/{th}"+str(i+1)+".jpg")
    #         imX = imgX.convert("RGB")
    #         imgs.append(imX)
    # im1.save(f"./{folder}/{folder}{th}.pdf", save_all=True, append_images=imgs)
    # print("Pictures Download & PDF conversion complete")
    # print("MP4 Downloading...",end='')
    # q = re.compile("main_\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\)\.mp4")
    # res2 = q.findall(atxt)
    # # print(type(imus))
    # # print(imus)
    # # print(type(res2))
    # # print(res2)
    # aurl = imus[0].replace("web_files","media_files") + "/" + res2[0]
    # # data = urllib.request.urlopen(url=aurl).read().decode()
    # # print(data)
    # urllib.request.urlretrieve(aurl, f"./{folder}/{th}audio.mp4")
