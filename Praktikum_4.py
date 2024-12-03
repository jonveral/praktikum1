# JUDUL PROGRAM
# Program untuk menemukan luas tanah terkecil yang memenuhi syarat 

# KAMUS
# banyak_data : integer
# luas_tanah : integer
# batas_min : integer

# ALGORITMA
# Input
banyak_data = int(input("Masukkan banyak data : "))
luas_tanah = [0] * banyak_data

for i in range(banyak_data):
    luas_tanah[i] = int(input(f"Masukkan luas tanah ke-{i+1}: "))

batas_min = int(input("Tentukan luas tanah minimum: "))

terkecil = None
for luas in luas_tanah:
    if luas >= batas_min:
        if terkecil is None or luas < terkecil:
            terkecil = luas

#Output
if terkecil is not None:
    print(f"Luas tanah terkecil yang dapat dipilih adalah {terkecil}.")
else:
    print("Tuan Leo tidak dapat membangun rumah.")