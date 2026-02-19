def hitung_nilai(nilai):
    total = 0
    for i in nilai:
        total += i
    
    rata_rata = total / len(nilai)
    
    if rata_rata >= 85:
        keterangan ="lulus dengan predikat A"
    elif rata_rata >= 75:
        keterangan = "lulus dengan predikat B"
    elif rata_rata >= 60:
        keterangan = "lulus dengan predikat C"
    else:
        keterangan = "tidak lulus"
   
    return rata_rata, keterangan

angka = [1, 2, 3, 4, 5]
total = 0
for i in angka:
    total += i  
print("Total : ", total)

data_nilai = [70, 67, 45, 98, 87]
rata_rata = hitung_nilai(data_nilai)
keterangan = hitung_nilai(data_nilai)