# NIM/NAMA : 16326039/PUTRI DAYITA SARASWATI
# TANGGAL : 29/10/2026
# DESKRIPSI : CASE 2

n = int(input("masukkan jumlah titik: "))
titik = [0 for i in range(n)]

for i in range(n):
    titik[i] = int(input("masukkan nilai titik ke-" + str(i+1) + ": "))
    
gunung = 0
lembah = 0

for i in range (1, n-1):
    if titik[i] > titik[i-1] and titik[i] > titik[i + 1]:
        gunung += 1
        
print("jumlah gunung: " + str(gunung))
print("jumlah lembah: " + str(lembah))

selalu_naik = True
selalu_turun = True
selalu_sama = True

for i in range(n - 1):
    if titik[i + 1] <= titik[i]:
        selalu_naik = False
    if titik[i + 1] >= titik[i]:
        selalu_turun = False
    if titik[i + 1] != titik[i]:
        selalu_sama = False

if selalu_naik:
    print("grafik selalu naik secara monoton")
elif selalu_turun: 
    print("grafik selalu turun secara monoton")
else:
    print("grafik selalu horizontal")