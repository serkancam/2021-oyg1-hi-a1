import sqlite3 as sql

no=int(input("okul no:"))
ad=input("ad:")
soyad=input("soyad:")
snf=int(input("sınıf:"))
sube=input("şube:")

vt = sql.connect("/home/serkan/Belgeler/2021-oyg1-hi-a1/veritabani/okul.db")
imlec=vt.cursor()
degerler=[no,ad,soyad,snf,sube]
ekleme_sorgu="insert into ogrenci values(?,?,?,?,?)"

imlec.execute(ekleme_sorgu,degerler)
vt.commit()
vt.close()