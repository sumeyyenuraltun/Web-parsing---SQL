import requests 
from bs4 import BeautifulSoup
from bs4 import Tag
import psycopg2
from db import db_olustur, tablo_olustur, db_baglanti

#WEB SCRAPING
response = requests.get("https://kur.doviz.com/") #siteye istek gönderir
#print(response) bu değer 200 ise sunucu isteği başarılı demektir.
#print(response.content)

veriler = []
#WEB PARSING
def web_parsing():
 soup = BeautifulSoup(response.content,"html.parser")
 tablo_verisi = soup.find_all("table",{"id":"currencies"}) #table verilerini alıyoruz

 kur_adi,alis,satis,enYuksek,enDusuk,degisim ='','','','','',''

 for kurlar in tablo_verisi:
  kur_verileri = kurlar.find_all("tr")
  # print(kur_verileri)
  for i in kur_verileri:
    kur_adi = i.find("div",{"class":"cname"}) #class adı cname olan verileri alıyoruz.
    kur_bilgileri = i.find_all("td") #satır verilerini alıyoruz.
    if len(kur_bilgileri)>=5:
      #satır verilerini tek tek atama yapıyoruz.
      alis = float(kur_bilgileri[1].text.strip().replace(",", "."))
      satis = float(kur_bilgileri[2].text.strip().replace(",", "."))
      enYuksek = float(kur_bilgileri[3].text.strip().replace(",", "."))
      enDusuk = float(kur_bilgileri[4].text.strip().replace(",", "."))
      degisim = float(kur_bilgileri[5].text.strip().replace(",", ".").replace("%","")) 

    if kur_adi:
     kur_adi = kur_adi.text.strip() #kur adlarını tek tek atama yapıyoruz.
     #print(kur_adi)
     veriler.append((kur_adi,alis,satis,enYuksek,enDusuk,degisim)) 

#DATABASE İŞLEMLERİ    
db_olustur()
tablo_olustur()

#DATABASE TABLOSUNA VERİ EKLEME İŞLEMİ
def veriyi_ekle():
 database_name ="dovizkuru_db"
 user_name= "postgres"
 password = "120322"
 host_ip = "127.0.0.1"
 host_port = "5432"
 baglanti =db_baglanti()
 cursor = baglanti.cursor()
 query_upsert = """
 INSERT INTO kur_tablosu (kur_adi, alis, satis, en_yuksek, en_dusuk, degisim)
 VALUES (%s, %s, %s, %s, %s, %s)
 ON CONFLICT (kur_adi) 
 DO UPDATE SET
    alis = EXCLUDED.alis,
    satis = EXCLUDED.satis,
    en_yuksek = EXCLUDED.en_yuksek,
    en_dusuk = EXCLUDED.en_dusuk,
    degisim = EXCLUDED.degisim
"""
 cursor.executemany(query_upsert, veriler)


#FLASK İLE ARAYÜZ
from flask import Flask, render_template,jsonify,request
from db import getDovizKuru, getFiltreliVeri

app = Flask(__name__)

doviz_kuru = getDovizKuru()

@app.route('/')
def home():
  doviz_kuru = getDovizKuru()
  return render_template("arayuz.html", doviz_kuru=doviz_kuru)

@app.route("/filtreli",methods= ["POST"])
def filtreli():
  min_alis = request.form.get("min_alis")
  max_alis = request.form.get("max_alis")
  min_dusuk = request.form.get("min_dusuk")
  max_dusuk= request.form.get("max_dusuk")
  min_degisim = request.form.get("min_degisim")
  max_degisim = request.form.get("max_degisim")
  doviz_kuru = getFiltreliVeri(min_alis,max_alis,min_dusuk,max_dusuk,min_degisim,max_degisim)
  return render_template("arayuz.html", doviz_kuru=doviz_kuru)


@app.route('/filtre_sifirla', methods=['GET'])
def filtre_sifirla():
  doviz_kuru = getDovizKuru()
  return render_template("arayuz.html", doviz_kuru=doviz_kuru)

app.run(debug=True)