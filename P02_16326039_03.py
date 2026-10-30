# NIM/NAMA : 16326039/PUTRI DAYITA SARASWATI
# TANGGAL : 15/10/2026
# DESKRIPSI : CASE 3

M = input("tipe mutan: ")
jumlah_armor = int(input("masukkan jumlah bone armor: "))
senjata = input("masukkan senjata: ")
kewarasan = int(input("masukkan kewarasan: "))

if M == "armsy":
    hp_mutan = 100
    damage_mutan = 100
elif tipe_mutan == "cowman": 
    hp_mutan = 80
    damage_mutan = 80 
elif tipe_mutan = "virginia":
    hp_mutan = 60
    damage_mutan = 65
    
nyawa_ky = 100
if M == "cowman" and kewaraswan < 40:
    damage_muatan += 25

pengurangan_armor = M*5
damage_diterima = damage_muatan - pengurangan_armor
if damage_diterima < 5:
    damage_diterima = 5
    
nyawa_ky -= damage_diterima

if nyawa_ky <= damage_diterima:
    print("tuan ky tewas di dalam gua")
else: 
    damage_serangan = 0
    
if senjata == "katana":
    damage_serangan = 40
    if kewarasan >= 80:
        damage_serangan = 70
elif senjata == "flare gun":
        damage_serangan = 25
    if tipe_muatann == "virginia" or tipe_muatan == "cowman":
        damage_serangan += 35
    if kewarasan < 30: 
        damage_serangan = 0
    
hp_mutan <= 0:
    print(f"mutan {M} berhasil kalah nyawa sisa {nyawa_ky}")
         