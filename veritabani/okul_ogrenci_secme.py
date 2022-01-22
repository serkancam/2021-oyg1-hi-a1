import sqlite3 as sql

no=int(input("okul no:"))

vt = sql.connect("/home/serkan/Belgeler/2021-oyg1-hi-a1/veritabani/okul.db")

imlec=vt.cursor()

sorgu_secme="select * from ogrenci where okul_no=?"

imlec.execute(sorgu_secme,[no])
kayitlar=imlec.fetchall()
# print(kayitlar)
for kayit in kayitlar:
    print(f"okul no:{kayit[0]}, ad:{kayit[1]},soyad:{kayit[2]},sınıf:{kayit[3]}-{kayit[4]}")
  

imlec.close()
vt.close()