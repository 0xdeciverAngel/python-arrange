import requests
from bs4 import BeautifulSoup
for i in range(1,5):
    url = "https://pttweb.tw/hot-threads?page="+str(i) #上一頁的網址

    
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select(".thread-title a") #標題
    #sel = soup.select(".thread-item a")
   # sel=[]
   # sel+=soup.find_all('span', {"class":"thread-title"})
  # s u = soup.select("div.btn-group.btn-group-paging a") #a標籤
    print ("本頁的URL為"+url)
    # url = "https://pttweb.tw/hot-threads?page="+str(i) #上一頁的網址
   # print(url)
    for s in sel: #印出網址跟標題
        # print(s["href"],s.text)
         print(s.text)
