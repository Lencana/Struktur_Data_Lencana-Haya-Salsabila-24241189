# Variabel number
number = "1234567890"

# a. Menampilkan data terakhir
print("Data terakhir:", number[-1]) 

# b. Menampilkan data pertama
print("Data pertama:", number[0])  

# c. Menampilkan data ke-3 sampai ke-6
print("Data ke-3 sampai ke-6:", number[2:6]) 

# Aplikasi Manipulasi Variabel Number
# Variabel number sesuai soal
number = "1234567890"

def menampilkan_data_terakhir(number):
    """A. Menampilkan data terakhir"""
    return number[-1]

def menampilkan_data_pertama(number):
    """B. Menampilkan data pertama"""
    return number[0]

def menampilkan_data_ke3_ke6(number):
    """C. Menampilkan data ke-3 sampai ke-6"""
    return number[2:6]

# Main program
print("Variabel number:", number)
print("A. Data terakhir:", menampilkan_data_terakhir(number))
print("B. Data pertama:", menampilkan_data_pertama(number))
print("C. Data ke-3 s/d ke-6:", menampilkan_data_ke3_ke6(number))