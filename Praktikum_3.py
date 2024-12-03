# JUDUL PROGRAM
# Program untuk menukar posisi angka dalam harga

# KAMUS
# jumlah_digit : integer
# harga : integer
# posisi1 : integer
# posisi2 : integer
# digit_count : integer
# digit1 : integer
# digit2 : integer

# ALGORITMA
jumlah_digit = int(input("Masukkan jumlah digit harga: "))
harga = int(input("Masukkan harga: "))

posisi1 = int(input("Masukkan posisi angka pertama yang akan ditukar: "))
posisi2 = int(input("Masukkan posisi angka kedua yang akan ditukar: "))

digit_count = 0
if harga == 0:
    digit_count = 1
else:
    if harga // 10 == 0:
        digit_count = 1
    elif harga // 100 == 0:
        digit_count = 2
    elif harga // 1000 == 0:
        digit_count = 3
    elif harga // 10000 == 0:
        digit_count = 4
    elif harga // 100000 == 0:
        digit_count = 5
    elif harga // 1000000 == 0:
        digit_count = 6
    elif harga // 10000000 == 0:
        digit_count = 7
    elif harga // 100000000 == 0:
        digit_count = 8
    elif harga // 1000000000 == 0:
        digit_count = 9
    else:
        digit_count = 10  # Anggap maksimal 10 digit untuk pembatasan

if digit_count != jumlah_digit:
    print("Masukan harga tidak valid")
else:
    if 1 <= posisi1 <= jumlah_digit and 1 <= posisi2 <= jumlah_digit:
        digit1 = (harga // (10 ** (jumlah_digit - posisi1))) % 10
        digit2 = (harga // (10 ** (jumlah_digit - posisi2))) % 10

        harga -= digit1 * (10 ** (jumlah_digit - posisi1))
        harga -= digit2 * (10 ** (jumlah_digit - posisi2))
        harga += digit1 * (10 ** (jumlah_digit - posisi2))
        harga += digit2 * (10 ** (jumlah_digit - posisi1))

        print(f"Harga setelah diperbaiki: {harga}")
    else:
        print("Posisi angka tidak valid.")
