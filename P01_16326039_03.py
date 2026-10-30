# Nama/NIM : PUTRI DAYITA SARASWATI
# Tanggal : 01 OKTOBER 2026
# Deskripsi : Problem 3

W = float(input("Masukkan berat muatan (ton): "))
Wmax = float(input("Masukkan kapasitas maksimal berat (ton): "))
v = float(input("Masukkan volume muatan (m3): "))
vmax = float(input("Masukkan kapasitas maksimal volume (m3): "))
s = float(input("Masukkan jarak tempuh (mil laut): "))
smax = float(input("Masukkan batas maksimal jarak (mil laut): "))
ab = float(input("Masukkan ambang efisiensi berat (persen): "))
av = float(input("Masukkan ambang efisiensi volume (persen): "))
t = float(input("Masukkan tarif operasional per mil laut: "))
sd = float(input("Masukkan subsidi efisiensi (persen): "))
status_aman = int(W <= Wmax) and (v <= vmax) and (s <= smax)
persen_w = (W/Wmax)*100
persen_v = (v/vmax)*100
status_efisien = int(bool(status_aman) and ((persen_w >= ab) or (persen_v >= av)))
biaya_dasar = s*t
total_biaya = biaya_dasar*(1 - (status_efisien*sd/100))

print(f"Status aman: {int(status_aman)}")
print(f"Status efisien: {status_efisien}")
print(f"total biayaa operasional: rp{total_biaya:.2f}")