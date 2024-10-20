total_nilai = 0
jumlah_nilai = 0

while True:
    nilai = input('Masukkan nilai : ')
    
    if nilai == "":
        break
    nilai = nilai.upper()
    
    if nilai not in ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]:
        print("Masukkan nilai dengan benar!")
    
    if nilai == "A":
        print("A = 4.00")
        total_nilai += 4.00
    elif nilai == "A-":
        print("A- = 3.75")
        total_nilai += 3.75
    elif nilai == "B+":
        print("B+ = 3.50")
        total_nilai += 3.50
    elif nilai == "B":
        print("B = 3.00")
        total_nilai += 3.00
    elif nilai == "B-":
        print("B- = 2.75")
        total_nilai += 2.75
    elif nilai == "C+":
        print("C+ = 2.50")
        total_nilai += 2.50
    elif nilai == "C":
        print("C = 2.00")
        total_nilai += 2.00
    elif nilai == "C-":
        print("C- = 1.75")
        total_nilai += 1.75
    elif nilai == "D":
        print("D = 1.50")
        total_nilai += 1.50
    elif nilai == "E":
        print("E = 1.25")
        total_nilai += 1.25
    else:
        print("Masukan nilai dengan benar!")
        
    jumlah_nilai += 1

if jumlah_nilai > 0:
    rata_rata = total_nilai / jumlah_nilai
    print(f"Rata - rata nilai : {rata_rata}")
else:
    print("Tidak ada nilai yang diinput")