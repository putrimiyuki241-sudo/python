#Program Geominer Sistem Indentifikasi Mineral
#Kelompok : 12 (Slavina Givlar Prihandani (16326075), Masyitha Syahirah Maharani (16326023), Vennesa Grasini Setiawan (16326323), Putri Dayita Saraswati (16326039), Cikal Rhazes Mahadewi (16326331))
#Mengidentifikasi mineral berdasarkan ciri fisik 

#KAMUS
#database_mineral : List of list
#kekerasan : float
#berat_jenis : float
#warna_gores : string
#kilap : string
#pecahan_input : string
#toleransi_k : float
#toleransi_bj : float
#jumlah_ditemuikan : int
#cocok_k : bool
#cocok_bj : bool
#cocok_gores : bool
#cocok_kilap : bool
#cocok_pecahan : bool

#Mengecek rentang nilai dengan toleransi
def cek_rentang(nilai_db, nilai_input, toleransi):
    if abs(nilai_db - nilai_input) <= toleransi:
        return True
    else:
        return False

#ALGORITMA PROGRAM UTAMA
print("=" * 50)
print("PROGRAM SISTEM IDENTIFIKASI MINERAL")
print("=" * 50)

#Input dari pengguna
kekerasan = float(input("Kekerasan Mohs: "))
warna_gores = input("Warna gores (putih, hitam kehijauan, abu-abu, merah coklat): ")
kilap = input("Jenis kilap (kaca, logam, mutiara): ")
pecahan_input = input("Pecahan/Belahan (tidak teratur, pecahan, sempurna, sangat sempurna): ")
berat_jenis = float(input("Berat Jenis: "))

#Inisialisasi variabel
jumlah_ditemukan = 0
toleransi_kekerasan = 0.5
toleransi_bj = 0.5

#Database Mineral
#Indeks: [0: Nama, 1: Kekerasan, 2:Gores, 3: Kilap, 4: Pecahan/Belahan, 5: Berat Jenis, 6: Deskripsi]
database_mineral = [
    ["Kuarsa (Quartz)", 7, "putih", "kaca", "pecahan", 2.65, "Mineral silikat yang sangat umum, keras, dan tahan terhadap pelapukan."],
    ["Feldspar (Ortoklas)", 6, "putih", "kaca", "sempurna", 2.56, "Mineral pembentuk batuan beku yang paling melimpah di kerak bumi."],
    ["Kalsit (Calcite)", 3, "putih", "kaca", "sempurna", 2.71, "Mineral karbonat utama penyusun batu kapur, bereaksi kuat dengan asam."],
    ["Pirit (Pyrite)", 6.5, "hitam kehijauan", "logam", "tidak teratur", 5, "Mineral sulfida besi dengan kilap logam kuning kuningan yang sering dikira emas."],
    ["Galena", 2.5, "abu-abu", "logam", "sempurna", 7.50, "Mineral bijih timbal utama yang memiliki berat jenis sangat tinggi dan belahan kubik."],
    ["Hematit", 6, "merah coklat", "logam", "pecahan", 5.26, "Mineral oksida besi yang terkenal dengan goresan khas berwarna merah kecoklatan."],
    ["Mika (Muskovit)", 2.5, "putih", "mutiara", "sangat sempurna", 2.80, "Mineral yang mudah mengelupas menjadi lembaran tipis yang elastis dan transparan."],
    ["Gipsum (Gypsum)", 2, "putih", "mutiara", "sempurna", 2.30, "Mineral evaporit yang lunak, bisa digores dengan kuku, sering dipakai untuk semen dan plester."]
]

#Jumlah data dalam database
N = len(database_mineral) 
#Inisialisasi pencacahan awal
i = 0

print("\n" + "=" * 50)
print("menganalisis karakteristik mineral...")
print("=" * 50 + "\n")

#Pemrosesan dengan pengulangan
while i < N:
    #Ekstraksi elemen dari baris database
    nama = database_mineral[i][0]
    k_db = database_mineral[i][1]
    gores_db = database_mineral[i][2]
    kilap_db = database_mineral[i][3]
    pecahan_db = database_mineral[i][4]
    bj_db = database_mineral[i][5]
    deskripsi = database_mineral[i][6]

    #Memanggil fungsi cek_rentang untuk angka
    cocok_k = cek_rentang(k_db, kekerasan, toleransi_kekerasan)
    cocok_bj = cek_rentang(bj_db, berat_jenis, toleransi_bj)

    #Pengecekan string
    cocok_gores = warna_gores.lower() in gores_db.lower()
    cocok_kilap = kilap.lower() in kilap_db.lower()
    cocok_pecahan = pecahan_input.lower() in pecahan_db.lower()

    #Analisis mineral
    if cocok_k and cocok_bj and cocok_gores and cocok_kilap:
        jumlah_ditemukan = jumlah_ditemukan + 1
        print("Nama Mineral: ", nama)
        print("Kekerasan: ", k_db)
        print("Warna Gores: ", gores_db)
        print("Kilap: ", kilap_db)
        print("Berat Jenis: ", bj_db)
        print("Pecahan/Belahan: ", pecahan_db)
        print("Deskripsi: ", deskripsi)
        print("-" * 50)

    i = i + 1

#Pengecekan hasil akhir
if jumlah_ditemukan == 0:
    print("Tidak ditemukan mineral yang mendekati kriteria tersebut.")