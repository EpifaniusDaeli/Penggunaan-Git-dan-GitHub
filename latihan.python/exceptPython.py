try:
    angka = int(input("Masukkan angka:"))
    
    Kuadrat = pow(angka, 2)
    print("Kuadrat = ", Kuadrat)
except ValueError:
    print("Input harus angka")
    
try:
    angka1 = int (input("Masukkan angka pertama:"))
    angka2 = int (input("Masukkan angka kedua:"))
    
    hasil = angka1 / angka2
    print("Hasil=", hasil)
    
except ValueError:
    print("Input harus angka")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")
