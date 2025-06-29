# Program untuk memisahkan string domain
# Input: cu.net

# Input dari pengguna
domain_lengkap = input("Masukkan nama domain anda: ")

# Pisahkan dengan delimiter titik (.)
nama, domain = domain_lengkap.split('.')

# Tampilkan hasil
print("Nama domain anda :", nama)
print("Domain yg anda gunakan :", domain)



# Program pemisahan string domain

# Input dari pengguna
domain_lengkap = input("Masukkan nama domain anda: ")

# Pisahkan berdasarkan tanda titik (.)
nama_domain, ekstensi = domain_lengkap.split(".")

# Tampilkan hasil
print("Nama domain anda :", nama_domain)
print("Domain yg anda gunakan :", ekstensi)