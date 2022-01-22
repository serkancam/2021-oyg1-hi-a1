# dosya = open("veriler.txt","r",encoding="utf-8")
# for s in dosya:
#     print(s,end="")

# dosya.close()

ad=input("ad:")
soyad=input("soyad")

dosya=open("veriler.txt","a",encoding="utf-8")

ekle = ad+","+soyad+"\n"

dosya.write(ekle)
dosya.close()