# NIM/NAMA : 16326039/PUTRI DAYITA SARASWATI
# TANGGAL  : 29/10/2026
# DESKRIPSI : CASE 3

n = int(input("masukkan jumlah kontainer: "))

t = [0 for i in range(n)]
d = [0 for i in range(n)]
p = [" " for i in range(n)]

for i in range (n):
    t[i] = int(input("masukkan waktu tiba kontainer ke-" + str(i + 1) + " (menit): "))
    d[i] = int(input("masukkan durasi bongkar kontainer ke-" + str(i + 1) + " (menit): " ))
    p[i] = input("masukkan prioritas kontainer ke-" + str(i + 1) + " (VIP/Regular): ")

selesai_dibongkar = [False for i in range(n)]
waktu_tunggu = [0 for i in range(n)]
urutan_bongkar = [ 0 for i in range(n)]

waktu_operasional = 0
jumlah_selesai = 0

while jumlah_selesai < n:
    terpilih = -1
    
    for i in range(n):
        if not selesai_dibongkar[i] and t[i] <= waktu_operasional:
            if terpilih == -1:
                terpilih = i
            else: 
                p1 = p[i]
                p2 = p[terpilih]
                
                if p1 == "VIP" and p2 == "Regular":
                    terpilih = i
                elif p1 == p2:
                    if d[i] < d[terpilih]:
                        terpilih = i
                    elif d[i] == d[terpilih]:
                        if t[i] < t[terpilih]:
                            terpilih = 1
                        elif t[i] == t[terpilih]:
                            if i < terplih:
                                terpilih = i

if terpilih == -1:
    min_tiba_berikutnya = -1
    for i in range(n):
        if not selesai_dibongkar[i]:
            if min_tiba_berikutnya == -1 or t[i] < min_tiba_berikutnya:
                min_tiba_berikutnya = t[i]
    waktu_operasional = min_tiba_berikutnya
else: 
    w_tunggu = waktu_operasional - t[terpilih]
    waktu_tunggu[terpilih] = w_tunggu
    waktu_operasional += d[terpilih]
    selesai_dibongkar[terpilih] = True
    
    urutan_bongkar[jumlah_selesai] = terpilih + 1
    jumlah_selesai += 1
    
str_urutan = ""
for i in range(n):
    str_urutan += str(urutan_bongkar[i])
    if i < n - 1:
        str_urutan += " "
print("urutan nomor kontainer yang dibongkar: " + str_urutan)
print("waktu selesai seluruh kontainer: " + str(waktu_operasional) + " menit")

total_tunggu = 0
for i in range(n): 
    total_tunggu += waktu_tunggu[i]
rata_tunggu = total_tunggu / n
print(f"rata-rata waktu tunggu: {rata_tunggu:.2f} menit")
max_tunggu = waktu_tunggu[0]
kontainer_max = 1

for i in range(1, n):
    if waktu_tunggu[i] > max_tunggu:
        max_tunggu = waktu_tunggu[i]
        kontainer_max = i + 1

print("waktu tunggu terlama: " + str(max_tunggu) + " menit (kontainer " + str(kontainer_max) + ")")
                    
                        
                    
            