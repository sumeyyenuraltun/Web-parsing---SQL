import psycopg2
database_name ="postgres"
user_name= "postgres"
password = "120322"
host_ip = "127.0.0.1"
host_port = "5432"

def db_baglanti():
   baglanti = psycopg2.connect(
            database = database_name,
            user = user_name,
            password= password,
            host = host_ip,
            port= host_port
        )
   return baglanti

def db_olustur(): 
        baglanti = db_baglanti()
        baglanti.autocommit = True
        cursor = baglanti.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='dovizkuru_db'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE dovizkuru_db WITH OWNER postgres")
        else:
            cursor.close()
            baglanti.close()

database_name ="dovizkuru_db"

def tablo_olustur():
 baglanti = db_baglanti()
 baglanti.autocommit = True
 cursor = baglanti.cursor()
 query_create_table = """
 CREATE TABLE IF NOT EXISTS kur_tablosu(
 kur_adi TEXT PRIMARY KEY,
 alis FLOAT,
 satis FLOAT,
 en_yuksek FLOAT,
 en_dusuk FLOAT,
 degisim FLOAT
 )
 """

 baglanti.autocommit = True
 cursor = baglanti.cursor()
 cursor.execute(query_create_table)

def getDovizKuru():
  baglanti = db_baglanti()
  cursor = baglanti.cursor()
  cursor.execute('SELECT kur_adi,alis,satis,en_yuksek,en_dusuk,degisim From public."kur_tablosu"')
  doviz_kuru = cursor.fetchall()
  cursor.close()
  baglanti.close()
  return doviz_kuru

def getFiltreliVeri(min_alis,max_alis,min_dusuk,max_dusuk,min_degisim,max_degisim):
  baglanti = db_baglanti()
  cursor = baglanti.cursor()
  cursor.execute('''
    SELECT kur_adi, alis, satis, en_yuksek, en_dusuk, degisim 
    FROM public."kur_tablosu" 
    WHERE alis BETWEEN %s AND %s 
    AND en_dusuk BETWEEN %s AND %s 
    AND degisim BETWEEN %s AND %s
''', (min_alis, max_alis, min_dusuk, max_dusuk, min_degisim, max_degisim))
  doviz_kuru = cursor.fetchall()
  cursor.close()
  baglanti.close()
  return doviz_kuru
