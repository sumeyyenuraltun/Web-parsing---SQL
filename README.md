Bu proje HTML tablo yapısı içeren bir Web sitesinden verileri çekerek bu verileri Python-PostgreSQL bağlantısı ile verileri veri tabanına kaydetmektedir. Kaydedilen veriler basit bir arayüzde gösterilmektedir ve arayüzde basit bir verileri filtreleme yapısı bulunmaktadır.

*KULLANLILAN TEKNOLOJİ VE KÜTÜPHANELER*  
request : Bu kütüphane HTTP isteği yaparak verileri almamızı sağlar.  
BeautifulSoup: Bu kütüphane ile HTML verileri parçalanıyor.(parsing işlemi)  
psycopg2: Bu kütüphane Python ve PostgreSQL arasında bağlantı sağlayarak veri tabanı oluşturma, tablo oluşturma ve sorgu işlemleri yapmak amacıyla kullanıldı.  
Flask, HTML,CSS: Web arayüzü geliştirmek amacıyla kullanıldı.  
SQL: SQL'i PostgreSQL üzerinde kullandım.  

*KURULUM*  
pip install flask requests beautifulsoup4 psycopg2  

*PROJE ÇALIŞMA AŞAMALARI*  
-request ve BeautifulSoup kullanılarak HTML tablosundaki veriler çekilir ve gerekli atama işlemi yapılarak veriler işlenir.  
-psycopg2 ile PostgreSQL-Python bağlantısı sağlanır.  
-Veri tabanı oluşturma,tablo oluşturma gibi işlemler yapılarak veriler tabloya kayıt edilir. Bu kısımda bu işlemler SQL cümleleri kullanılarak yapıldı ve fonksiyonel hale getirmek için veri tabanının daha önce olup olmadığına bakıldı. Eğer veri tabanı daha önce yoksa önce veri tabanı oluştuurldu ve veriler kaydedildi, eğer veri tabanı daha önceden varsa kaydedilen verileri anlık olarak güncellemek üzerine kod yazıldı.  
-Arayüz oluşturmak için Flask kullanıldı.   
-Arayüze filtreleme seçeneği koydum ve SQL sorguları yaparak verileri filtreleyebiliyorum.  

*VERİ KAYNAK LİNKİ*  
https://kur.doviz.com/  

*UYGULAMA GÖRÜNTÜLERİ*  

![image](https://github.com/user-attachments/assets/3a7ed48e-8987-4954-8dee-168071017794)
FİLTRELENMİŞ VERİLER  
5,1 - 38,9  
5 - 39  
-0,1 - 0,7  
![image](https://github.com/user-attachments/assets/94e6cdab-3631-4c45-a2e9-3eff2ff1d66f)

*KULLANDIĞIM KAYNAKLAR*  
https://youtu.be/T4EXSBMicBY?si=xKsFMXLZPpfy10VA  
https://youtu.be/vmfhnChPpnA?si=3wAveg_iNhhjlmkI  
https://www.youtube.com/watch?v=6hR0VDVEPFk&list=PPSV  







