#1
while True:
    try:
     angka = int(input("Masukkan angka:"))
     break
    except ValueError:
        print("Input harus angka")
    

Kuadrat = pow(angka, 2)
print("Kuadrat = ", Kuadrat)
S
    
#2
while True:   
  try:
    angka1 = int (input("Masukkan angka pertama:"))
    break
  except ValueError:
    print("Input harus angka")
while True:
  try:
    angka2 = int (input("Masukkan angka kedua:"))
    break
  except ValueError:
    print("Input harus angka")

try:
    hasil = angka1 / angka2
    print("Hasil=", hasil)
    
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")
    
#3

while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        break
    except ValueError:
        print("Input harus angka")


while True:
    operator = input("Masukkan operator (+, -, *, /): ")

    if operator in ['+', '-', '*', '/']:
        break
    else:
        print("Operator tidak valid. Masukkan operator yang benar")


while True:
    try:
        angka2 = int(input("Masukkan angka kedua: "))
        break
    except ValueError:
        print("Input harus angka")


try:
    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        hasil = angka1 / angka2

    print("Hasil =", hasil)

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")

#4
while True:
    print("\n===MENU===")
    print("1.Hitung Luas persegi")
    print("2.Hitung Luas persegi panjang")
    print("3.Keluar")

    try:
        p = int(input("Pilih menu(1-3): "))
    except ValueError:
        print("Menu Tidak Valid. Masukkan menu yang benar")
        continue

    if p == 1:
        while True:
            try:
                sisi = int(input("Masukkan sisi persegi:"))
                break
            except ValueError:
                print("Input harus angka")

        luas_persegi = sisi * sisi
        print(f"Luas persegi: {luas_persegi} cm")

    elif p == 2:   # ← PERHATIKAN INI
        while True:
            try:
                panjang = int(input("Masukkan Panjang: "))
                break
            except ValueError:
                print("Input harus angka")

        while True:
            try:
                lebar = int(input("Masukkan Lebar: "))
                break
            except ValueError:
                print("Input harus angka")

        luas_persegi_panjang = panjang * lebar
        print(f"Luas persegi panjang: {luas_persegi_panjang} cm²")

    elif p == 3:
        print("Program selesai")
        break
    else:
        print("Menu Tidak Tersedia")