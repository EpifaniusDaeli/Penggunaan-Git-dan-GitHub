class Mobil:
    def __init__(self, merek, warna, tahun):
        self.merek = merek
        self.warna = warna
        self.tahun = tahun
    def info(self):
        print(f"Mobil {self.merek} berwarna {self.warna} tahun {self.tahun}")
    
    
m1 = Mobil("Toyota", "hitam", 2020)
m1.info()


class Hewan:
    def __init__ (self, nama):
        self.nama = nama
    def bersuara(self):
        print(f"{self.nama} hewan bersuara")

class Kucing(Hewan):
    def meong(self):
        print(f"{self.nama} Meong!")
        
k1 = Kucing("Kitty")
k1.bersuara()
k1.meong()
