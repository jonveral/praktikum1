# JUDUL PROGRAM
# Program untuk memastikan setiap pengunjung hanya mendapat konsumsi sekali

# ALGORITMA
# Array untuk melacak tiket yang sudah mendapat konsumsi
tiket_diserahkan = []  # List untuk menyimpan nomor tiket
tiket_ganda = 0        # Untuk menghitung tiket yang mencoba lebih dari sekali
total_pengunjung = 0   # Untuk menghitung total pengunjung yang dilayani

# Loop untuk memasukkan nomor tiket
selesai = False
while not selesai:
    tiket = input("Masukkan nomor tiket pengunjung: ")
    
    if tiket == "XXX":
        selesai = True
    else:
        # Periksa apakah tiket sudah ada di array tiket_diserahkan
        if tiket in tiket_diserahkan:
            tiket_ganda += 1
            print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
        else:
            # Menambahkan tiket baru ke array tiket_diserahkan
            tiket_diserahkan += [tiket]  # Tidak menggunakan `.append()`
            total_pengunjung += 1
            print("Pengunjung tersebut bisa mendapat konsumsi.")

# Menampilkan hasil
print(f"Total pengunjung yang mendapat konsumsi: {total_pengunjung}")
print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {tiket_ganda}")
