total_harga = 0

while True:
    umur = input("Input umur : ")

    if umur == '':
        break

    try:
        umur = int(umur)
    except ValueError:
        print("Input tidak valid. Masukkan angka umur.")
        continue

    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        total_harga += harga
        print(f"Harga: ${harga}")
    elif umur >= 65:
        harga = 18
        total_harga += harga
        print(f"Harga: ${harga}")
    else:
        harga = 23
        total_harga += harga
        print(f"Harga: ${harga}")

    print(f"Total : ${total_harga}")

while True:
    try:
        bayar = float(input("Input uang: "))
        if bayar < 0:
            print("Input uang tidak bisa negatif. Coba lagi.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Masukkan jumlah uang dalam format yang benar.")

print(" " " " * 15 + "_____________Pembayaran_________")  
if bayar > total_harga:
    kembalian = bayar - total_harga
    print( " " " " * 15 + f"Total: ${total_harga}\n" +
           " " " " * 15 + f"Uang: ${bayar}\n" +
           " " " " * 15 + f"Kembalian: ${kembalian:.2f}")
elif bayar == total_harga:
    print( " " " " * 15 + f"Total: ${total_harga}\n" +
           " " " " * 15 + f"Uang: ${bayar}\n" +
           " " " " * 15 + "Tidak ada kembalian.")
else:
    kekurangan = total_harga - bayar
    print(" " * 15 + f"\nUang yang Anda bayar kurang. Anda masih kurang: ${kekurangan:.2f}")

print(f"\nTotal akhir: ${total_harga}")
