#Latihan

#1
def hitung_maksimal(data):
    maksimal = data[0]
    for i in data:
        if i > maksimal:
            maksimal = i
    return maksimal

data = []
for i in range(10):
    angka = int(input("Masukkan data: "))
    data.append(angka)

hasil = hitung_maksimal(data)   
print("Nilai maksimal adalah:", hasil)

#2
nilai = [76, 85, 90, 92, 88]
lulus = 0
tidak_lulus = 0 

for i in nilai:
    if i >= 75:
        lulus += 1
    else:
        tidak_lulus += 1
        
print("Jumlah nilai lulus:", lulus)
print("Jumlah nilai tidak lulus:", tidak_lulus)

#3
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
    def rata_rata(self):
        total = 0
        for i in self.nilai:
            total += i
            
        rata_rata = total / len(self.nilai)
        return rata_rata
    
    def status(self):
        rata_rata = self.rata_rata()
        if rata_rata >=75:
            return "lulus"
        else:
            return "tidak lulus"
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Rata-rata: {self.rata_rata()}")
        print(f"Status: {self.status()}")
m1 = Mahasiswa ("Epifanius daeli", "250711207144", [95, 96, 97, 89, 87, 85] )
m1.info()

#4
class BangunDatar:
    def menghitung_luas(self):
        print("Menghitung luas bangun datar")
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    def hitung_luas_persegi(self):
        Luas = self.sisi * self.sisi
        print(f"Luas Persegi : {Luas}")
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def hitung_luas(self):
        Luas = self.panjang * self.lebar
        print(f"Luas Persegi Panjang: {Luas}")

p1 = Persegi(7)
p1.luas()

p2 = PersegiPanjang(6, 3)
p2.luas()