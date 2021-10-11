# parker_uzay_araci.py
# parker uzay aracının hızı saniyede 150km
# ekvator yarıçapı=6378 km
# kutup yarıçapı=6357 km

ekvator_yaricapi = 6378
kutup_yaricapi = 6357
pi = 3.14
parker_hizi = 150

ekvator_cevresi =2*pi*ekvator_yaricapi
kutup_cevresi = 2*pi*kutup_yaricapi

ekvator_suresi_sn =ekvator_cevresi/parker_hizi
kutup_suresi_sn =kutup_cevresi/parker_hizi

print(f"parker uzay aracı ekvator çevresini {ekvator_suresi_sn} saniyede dolaşır.")
print(f"parker uzay aracı kutup çevresini {kutup_suresi_sn} saniyede dolaşır.")

# bu süreyi dakika ve saniyeye çeviriniz
print(f"{ekvator_suresi_sn//60} dakika {ekvator_suresi_sn%60}")
