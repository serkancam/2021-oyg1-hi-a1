while True:
    try:
        s1=int(input("1. sayıyı giriniz:"))
        s2=int(input("2. sayıyı giriniz:"))
        sonuc = s1/s2
        print("Bu satırları okuyorsan hatasızsındır.")
        break
    except ValueError:
        print("Lütfen sadece tam sayı giriniz")
        continue
    except ZeroDivisionError:
        print("sıfıra bölme hatası")
        continue
       




print(f"{s1}/{s2}={sonuc}")