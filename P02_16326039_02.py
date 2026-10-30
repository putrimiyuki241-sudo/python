# NIM/NAMA : 16326039/PUTRI DAYITA SARASWATI
# TANGGAL : 15/10/2026
# DESKRIPSI : CASE 2

C = float(input("masukkan konsentrasi CO2: "))
suhu = float(input("masukkan suhu ruangan (C): "))
kelembapan_udara = float(input("masukkan kelembapan udara (persen): "))

if C <= 600:
    print("normal")
elif C <= 1000: 
    print("waspada")
else: 
    print("bahaya")
    
if suhu <= 20:
    print("dingin")
elif suhu <= 25:
    print("ideal")
else:
    print("panas")
    
if kelembapan_udara <= 40:
    print("kering")
elif kelembapan_udara <= 60:
    print("ideal")
else: 
    print("lembap")
    
if C == "bahaya":
    print("evakuasi dan nyalakan exhaust fan maksimal")
elif C == "panas":
    if suhu == "panas":
        print("nyalakan ventilasi dan ac pendingin")
    elif suhu == "dingin":
        print("nyalakan ventilasi dan pemanas ruangan")
    elif suhu == "ideal":
        print("nyalakan ventillasi")
elif C == "normal":
    if suhu == "ideal" and kelembapan_udara == "ideal":
        print("kondisi ruangan nyaman")
    elif suhu == "panas" and kelembapan_udara == "lembap":
        print("nyalakan ac dan dehumidifier")
    elif suhu == "panas" and kelembapan_udara != "lembap":
        print("nyalakan ac")
    elif suhu == "dingin" and kelembapan_udara == "kering":
        print("nyalakan pemanas dan humidifier")
    elif suhu == "dingin" and kelembapan_udara != "kering":
        print("nyalakan pemanas")
    elif suhu == "ideal" and kelembapan_udara == "lembap":
        print("nyalakan dehumidifier")
    elif suhu == "ideal" and kelembapan_udara == "kering":
        print("nyalakan humidifier") 
        