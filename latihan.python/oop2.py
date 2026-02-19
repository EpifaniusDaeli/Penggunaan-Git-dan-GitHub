class Hewan:
    def makan(self):
        print("Hewan sedang makan")
class Anjing(Hewan):
    def makan(self):
        print("Anjing sedang makan")
        
a1 = Anjing()
a1.makan()

#Latihan

#1
def hitung_maksimal(data):
    data = []
    while i < 10:
        data.append(int(input("Masukkan data:")))
        i += 1
    maksimal = data[0]
    for i in data:
        if i > maksimal:
            maksimal = i
    return maksimal 