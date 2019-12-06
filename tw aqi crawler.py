import requests
import json
# from bs4 import BeautifulSoup
login_url = 'https://taqm.epa.gov.tw/taqm/iotHandler.ashx?act=M60&SiteId=21'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
so2 = ""
co=""                                                                               
o3=""
no2=""
def rep_web():
    response = requests.get(login_url,headers)
    print(response)
    json_d = json.loads(response.text)
    so2 = json_d["Data"][0]["SO2"]
    co =json_d["Data"][0]["CO"]
    o3 =json_d["Data"][0]["O3"]
    no2=json_d["Data"][0]["NO2"]
    print(json_d["Result"])
    print(json_d["SiteId"])
    print(json_d["SysDate"])
    print("SO2:",(json_d["Data"][0]["SO2"]))
    print("CO:",json_d["Data"][0]["CO"])
    print("O3:",json_d["Data"][0]["O3"])
    print("NO2:",json_d["Data"][0]["NO2"])
    print(json_d["Data"][0]["DATA_TIME"])
    print(json_d["Data"][0]["Time"])

rep_web()

# print("aaa\naaa")