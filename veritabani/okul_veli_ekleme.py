import sqlite3 as sql

ogrenci_no=int(input("okul no:"))
veli_no=int(input("veli no:"))
ad=input("ad:")
soyad=input("soyad:")


vt = sql.connect("/home/serkan/Belgeler/2021-oyg1-hi-a1/veritabani/okul.db")
imlec=vt.cursor()
degerler=[ogrenci_no,veli_no,ad,soyad]
ekleme_sorgu="insert into veli values(?,?,?,?)"

imlec.execute(ekleme_sorgu,degerler)
vt.commit()
imlec.close()
vt.close()