# buatlah program perhitungan luas 
masukkan = input("apakah anda ingin menghitung persegi atau segitiga?")
#pesegi
panjang = int(input("masukan panjang"))
lebar = int(input("masukan lebar"))
luas = panjang*lebar
print(f"luas persegi = {luas}")
#segitiga
alas = int(input("masukkan alas"))
tinggi = int(input("masukkan tinggi"))
luas = 1/2*alas*tinggi
print(f"luas segitiga = {luas}")
