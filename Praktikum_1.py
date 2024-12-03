# JUDUL PROGRAM
# Menentukan nilai akhir berdasarkan rata-rata 3 kuis

# KAMUS
# kuis1      :  float
# kuis2      :  float
# kuis3      :  float
# rata_rata  :  float

# ALGORTIMA
kuis1 = float(input("Masukkan nilai kuis pertama: "))
kuis2 = float(input("Masukkan nilai kuis kedua: "))
kuis3 = float(input("Masukkan nilai kuis ketiga: "))

rata_rata = (kuis1 + kuis2 + kuis3) / 3

if rata_rata >= 80:
    print("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif rata_rata >= 70:
    print("Tuan Leo mendapatkan nilai Lulus.")
else:
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")
