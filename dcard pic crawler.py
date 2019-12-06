import requests
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
#####################################



#####################################
res = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
url=input("in:")
# url="https://www.dcard.tw/f/pet/p/232629446-%E5%8E%AD%E4%B8%96%E7%9A%84%E5%8D%A1%E7%B4%8D%E8%83%96%E6%8B%89"
r = requests.get(url, headers)
soup = BeautifulSoup(r.text, "html.parser")
s = soup.select(".GalleryImage_image_3lGzO5")
# s=soup.find_all( {"class":"thread-title"})
for i in s:
    # print(i)
    # print(i["src"], i.text)
    print(i["src"])
    res.append(i["src"])
################################
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3')]
urllib.request.install_opener(opener)
################################


for i in res:
    print(i)
    x=i.split('/')[-1]
    local = os.path.join('A:\\%s.jpg' % x)
    urllib.request.urlretrieve(i,local) #link是下載的網址 local是儲存圖片的檔案位址.
    


