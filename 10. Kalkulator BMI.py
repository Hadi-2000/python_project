def hitung_bmi():
    try:
        tinggi = input("Masukan tinggi badan anda dalam cm : ").strip()
        berat = input("Masukan berat badan anda dalam kg : ").strip()

        if not berat or not tinggi:
            raise ValueError("Error: Data tidak boleh kosong.")
        
        if not berat.replace('.','').isdigit() or not tinggi.replace('.','').isdigit():
            raise ValueError("Error: Inputan harus angka.")
        
        berat = float(berat)
        tinggi = float(tinggi)

        if berat <= 0 or tinggi <= 0:
            raise ValueError("Error: Berat/Tinggi harus > 0.")

        tinggi_m = tinggi/100
        
        bmi = berat/(tinggi_m**2)
        print(f"BMI Anda : {bmi:.2f}")

        if bmi < 18.5 :
            print("Kategori : Underweight")
        elif 18.5 <= bmi or bmi < 25 :
            print("Kategori : Normal Wight")
        elif 25 <= bmi or bmi < 30 :
            print("Kategori : Overweight")
        elif bmi >= 30:
            print("Kategori : Obesitas")
        else:
            print("Data tidak terdefinisi")
    except ValueError:
        print("Error: Data yang dimasukan harus berupa angka positif")

if __name__ == "__main__":
    while True:
        hitung_bmi()
        ulangi = input("Apakah ingin mengulangi : (Y/N)").upper()
        if ulangi == 'N':
            break