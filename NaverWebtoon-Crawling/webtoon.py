# [!] 스터디 목적으로 만든 웹툰 다운로더입니다. 악용 시 걸리는 문제에 대해 제작자는 책임을 지지 않습니다.
import urllib.request

from bs4 import BeautifulSoup
import os
import glob
from PIL import Image

#Access Denied?
open_naver = urllib.request.build_opener()
open_naver.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')]
urllib.request.install_opener(open_naver)

URL = urllib.request.urlopen('https://comic.naver.com/webtoon/detail?titleId=783054&no=27&weekday=tue')
soup = BeautifulSoup(URL.read(), "html.parser")
URL.close()

webtoon_title = soup.find("div", {"class", "detail"}).find("h2").text.split()[0]
print("웹툰 제목: " + webtoon_title)
print("=====================================")

os.chdir("./images")
if not os.path.isdir(webtoon_title):
    print("[~] 다운로드 할 새로운 폴더를 생성합니다.")
    os.mkdir(webtoon_title)
    print("[~] " + webtoon_title + " 작품의 저장 폴더를 생성 완료하였습니다.")
else:
    print("[~] 같은 이름의 폴더가 이미 존재합니다.")

os.chdir("./" + webtoon_title)

site_div = soup.find("div", {"class", "wt_viewer"})
site_img = site_div.findAll("img")

webtoon_count = 1
for count in site_img:
    download_path = count.get("src")
    if(webtoon_count < 10):
        img_num = "0" + str(webtoon_count) + ".jpg"
        urllib.request.urlretrieve(download_path, img_num)
    else:
        img_num = str(webtoon_count) + ".jpg"
        urllib.request.urlretrieve(download_path, img_num)
    webtoon_count += 1
print("[~] 다운로드가 완료되었습니다.")