# NIM/NAMA : 16326039/PUTRI DAYITA SARASWATI
# TANGGAL : 29/10/2026
# DESKRIPSI : CASE 1

n = int(input("masukkan jumlah peserta: "))
waktu = [0 for i in range(n)]

for i in range(n):
    waktu [i] = float(input("Masukkan waktu tempuh peserta yang ke-" + str(i+1) + " (menit): "))
    
waktu_tercepat = waktu[0]
for i in range (1, n):
    if waktu[i] < waktu_tercepat:
        waktu_tercepat = waktu[i]
        
waktu_mik = waktu[0]
lebih_cepat = 0

for i in range(n):
    if waktu[i] < waktu_mik:
        lebih_cepat += 1

peringkat_mik = lebih_cepat + 1

print("waktu tercepat dalam lomba lari adalah " + str(waktu_tercepat) + " menit")
print("tuan mik peringkat ke-" + str(peringkat_mik) + " dari " + str(n) + " peserta")
    