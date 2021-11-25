#Input awal
print("======== Calculator sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat \n")

pilihan = int(input("Masukkan pilihan: "))
angka1 = int(input("Masukkan bilangan 1: "))
angka2 = int(input("Masukkan bilangan 2: " ))

#Function macem"
def tambah(b1,b2):
    return b1 + b2

def kurang(b1,b2):
    return b1 - b2

def bagi(b1,b2):
    return b1/b2

def kali(b1,b2):
    return b1*b2

def pangkat(b1,b2):
    return b1**b2

def calculator():
    if pilihan ==1:
        print("Hasilnya: ", tambah(angka1, angka2))
    elif pilihan ==2:
        print("Hasilnya: ", kurang(angka1, angka2))
    elif pilihan ==3:
        print("Hasilnya: ", kali(angka1, angka2))
    elif pilihan ==4:
        print("Hasilnya: ", bagi(angka1, angka2))
    elif pilihan ==5:
        print("Hasilnya: ", pangkat(angka1, angka2))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

calculator()
