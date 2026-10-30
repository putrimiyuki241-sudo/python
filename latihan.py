P = int(input("Masukkan daya lampu (watt): "))
s = int(input("Lama waktu menyala (jam): "))
t = int(input("Masukkan tarif listrik (rupiah per kWh): "))
energi = P*s / 1000
biaya = energi*t 
print(f"Biaya listrik yang terbuang adalah Rp{biaya}")
