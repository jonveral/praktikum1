# JUDUL PROGRAM
# Membagikan hadiah lomba lari kepada peserta yang terkualifikasi

# KAMUS
# N                       :  integer
# T                       :  integer
# waktu_leo               :  integer
# waktu_deb               :  integer
# waktu_sal               :  integer
# peserta_terkualifikasi  :  integer
# hadiah_per_peserta      :  integer

# ALGORITMA
N = int(input("Masukkan nilai N: "))
T = int(input("Masukkan nilai T: "))
waktu_leo = int(input("Masukkan waktu lari Tuan Leo: "))
waktu_deb = int(input("Masukkan waktu lari Nona Deb: "))
waktu_sal = int(input("Masukkan waktu lari Nona Sal: "))

peserta_terkualifikasi = 0
if waktu_leo <= T:
    peserta_terkualifikasi += 1
if waktu_deb <= T:
    peserta_terkualifikasi += 1
if waktu_sal <= T:
    peserta_terkualifikasi += 1

if peserta_terkualifikasi > 0:
    hadiah_per_peserta = N // peserta_terkualifikasi
    print(f"Terdapat {peserta_terkualifikasi} peserta yang terkualifikasi dan masing-masing akan mendapatkan {hadiah_per_peserta} dollar kompeng.")
else:
    print("Tidak ada peserta yang terkualifikasi.")
