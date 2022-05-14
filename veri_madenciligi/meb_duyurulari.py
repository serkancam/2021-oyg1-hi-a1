from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import pandas as pd
import time
ayarlar = FirefoxOptions()
ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar, executable_path="/home/serkan/Belgeler/2021-oyg1-hi-a1/geckodriver")
surucu.get("http://www.meb.gov.tr/meb_duyuruindex.php")
# icerik=surucu.page_source
# print(icerik)
# surucu.close()
aciklama=[]
tarih=[]
adres=[]
sayfa=1
son_sayfa=61
while sayfa<=son_sayfa:
    icerik=surucu.page_source
    agac=BeautifulSoup(icerik,"lxml")
    duyurular=agac.find_all("tr",attrs={"role":"row"})
    for duyuru in duyurular:
        try:
            duyuru_baslik=duyuru.find_all("td")[1].text
            duyuru_adres=duyuru.find_all("td")[1].find("a").get("href")
            duyuru_tarih=duyuru.find_all("td")[2].text            
            tarih.append(duyuru_tarih)
            adres.append(duyuru_adres)
            aciklama.append(duyuru_baslik)
        except:
            continue
    surucu.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a").click()
    sayfa=sayfa+1
    time.sleep(1)

veri={"aciklama":aciklama,"adres":adres,"tarih":tarih}
df=pd.DataFrame(veri)
df.to_csv("meb_duyuru4.csv",index=False)
print("işlem bitti.")
surucu.close()
