# JUDUL PROGRAM
# Program untuk memastikan setiap pengunjung hanya mendapat konsumsi sekali

# ALGORITMA
tiket_diserahkan = []  
tiket_ganda = 0        
total_pengunjung = 0   

selesai = False
while not selesai:
    tiket = input("Masukkan nomor tiket pengunjung: ")
    
    if tiket == "XXX":
        selesai = True
    else:
        if tiket in tiket_diserahkan:
            tiket_ganda += 1
            print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
        else:
            tiket_diserahkan += [tiket]  
            total_pengunjung += 1
            print("Pengunjung tersebut bisa mendapat konsumsi.")

print(f"Total pengunjung yang mendapat konsumsi: {total_pengunjung}")
print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {tiket_ganda}")
