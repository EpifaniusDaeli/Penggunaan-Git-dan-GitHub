def hitung_nilai(data_nilai):
    total = 0
    for i in data_nilai:
        total += i
    
    rata_rata = total / len(data_nilai)
    
    if rata_rata >= 85:
        keterangan ="lulus dengan predikat A"
    elif rata_rata >= 75:
        keterangan = "lulus dengan predikat B"
    elif rata_rata >= 60:
        keterangan = "lulus dengan predikat C"
    else:
        keterangan = "tidak lulus"
   
    return rata_rata, keterangan

data_nilai = [100, 100, 100, 100, 100, 98, 98, 98, 98, 98]
rata_rata, keterangan = hitung_nilai(data_nilai)
print("Rata-rata:", rata_rata)
print("Keterangan:", keterangan)
    