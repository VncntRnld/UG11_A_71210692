kal = input("Masukkan Kalimat: ")
m = int(input("Index Start: "))
s = int(input("Index Stop: "))

def hitung_hapus(k,b1,b2):
    return max(0, (b2 - b1 + 1) / int(len(k)) * 100)

print(hitung_hapus(kal,m,s))