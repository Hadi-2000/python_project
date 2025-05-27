print('konverter suhu sederhana')
print('C = Celsius, F = Fahrenheit, R = Reaumur, K = Kelvin')
i = 0
hasil = 0
hasil = int(hasil)

while i == 0:
    j = 0
    awal = input('Masukan angka suhu awal : ')
    tem_awal = input('Masukan derajat suhu awal : ').upper()
    tem_akhir = input('Mau diubah ke derajat suhu apa : ').upper()

    # Validasi input angka
    try:
        awal = float(awal)
    except ValueError:
        print('Input harus berupa angka!')
        continue

    awal = int(awal)
    if(tem_awal == 'C'):
        if(tem_akhir == 'C'):
            print(f'Hasil perubahan subu dari {awal} Celsius = {awal} Celsius')
            print('Hasilnya sama dikarenakan derajat awal = derajat akhir')
        elif(tem_akhir == 'F'):
            hasil = (awal/5*9)+32
            print(f'Hasil perubahan subu dari {awal} Celsius = {hasil} Fahrenheit')
        elif(tem_akhir == 'R'):
            hasil = awal/5*4
            print(f'Hasil perubahan subu dari {awal} Celsius = {hasil} Reaumur')
        elif(tem_akhir == 'K'):
            hasil = awal+273.15
            print(f'Hasil perubahan subu dari {awal} Celsius = {hasil} Kelvin')
        else:
            print('Data derajat suhu target tidak ditemukan')
    elif(tem_awal == 'R'):
        if(tem_akhir == 'C'):
            hasil = awal/4*5
            print(f'Hasil perubahan subu dari {awal} Reaumur = {hasil} Celsius')
        elif(tem_akhir == 'F'):
            hasil = (awal/4*9)+32
            print(f'Hasil perubahan subu dari {awal} Reaumur = {hasil} Fahrenheit')
        elif(tem_akhir == 'R'):
            print(f'Hasil perubahan subu dari {awal} Reaumur = {awal} Reaumur')
            print('Hasilnya sama dikarenakan derajat awal = derajat akhir')
        elif(tem_akhir == 'K'):
            hasil = (awal/4*5)+273.15
            print(f'Hasil perubahan subu dari {awal} Reaumur = {hasil} Kelvin')
        else:
            print('Data derajat suhu target tidak ditemukan')

    elif(tem_awal == 'F'):
        if(tem_akhir == 'C'):
            hasil = (awal-32)/9*5
            print(f'Hasil perubahan subu dari {awal} Fahrenheit = {hasil} Celsius')
        elif(tem_akhir == 'F'):
            print(f'Hasil perubahan subu dari {awal} Fahrenheit = {awal} Fahrenheit')
            print('Hasilnya sama dikarenakan derajat awal = derajat akhir')
        elif(tem_akhir == 'R'):
            hasil = (awal-32)/9*4
            print(f'Hasil perubahan subu dari {awal} Fahrenheit = {hasil} Reaumur')
        elif(tem_akhir == 'K'):
            hasil = ((awal-32)/9*5)+273.15
            print(f'Hasil perubahan subu dari {awal} Fahrenheit = {hasil} Kelvin')
        else:
            print('Data derajat suhu target tidak ditemukan')

    elif(tem_awal == 'K'):
        if(tem_akhir == 'C'):
            hasil = awal - 273.15
            print(f'Hasil perubahan subu dari {awal} Kelvin = {hasil} Celsius')
        elif(tem_akhir == 'F'):
            hasil = ((awal - 273.15)/5*9)+32
            print(f'Hasil perubahan subu dari {awal} Kelvin = {hasil} Fahrenheit')
        elif(tem_akhir == 'R'):
            hasil = (awal - 273.15)/5*4
            print(f'Hasil perubahan subu dari {awal} Kelvin = {hasil} Reaumur')
        elif(tem_akhir == 'K'):
            print(f'Hasil perubahan subu dari {awal} Kelvin = {awal} Kelvin')
            print('Hasilnya sama dikarenakan derajat awal = derajat akhir')
        else:
            print('Data derajat suhu target tidak ditemukan')

    else:
        print('Data derajat suhu yang dimasukan tidak ditemukan')
        
    while j == 0:   
        ulang = input('Apakah anda ingin melakukannya lagi : (Y/N)')
        if(ulang.upper() == 'Y'):
            j = 1
        elif(ulang.upper() == 'N'):
            print('Program sudah ditutup')
            i = 1
            j = 1
            exit()
        else:
            print('Data yang diinput tidak terdefinisi')
        
 
#kalau versi benarnya
#def konversi_suhu():
#     print('Konverter Suhu Sederhana\n[C]elsius, [F]ahrenheit, [R]eaumur, [K]elvin')
    
#     while True:
#         try:
#             suhu = float(input('Masukkan suhu awal: '))
#             satuan_awal = input('Satuan awal (C/F/R/K): ').upper()
#             satuan_tujuan = input('Satuan tujuan (C/F/R/K): ').upper()
            
#             if satuan_awal not in ['C','F','R','K'] or satuan_tujuan not in ['C','F','R','K']:
#                 print('Error: Satuan tidak valid!')
#                 continue
                
#             # Konversi ke Celsius dulu sebagai dasar
#             if satuan_awal == 'C':
#                 celsius = suhu
#             elif satuan_awal == 'F':
#                 celsius = (suhu - 32) * 5/9
#             elif satuan_awal == 'R':
#                 celsius = suhu * 5/4
#             elif satuan_awal == 'K':
#                 celsius = suhu - 273.15
            
#             # Konversi dari Celsius ke satuan tujuan
#             if satuan_tujuan == 'C':
#                 hasil = celsius
#             elif satuan_tujuan == 'F':
#                 hasil = celsius * 9/5 + 32
#             elif satuan_tujuan == 'R':
#                 hasil = celsius * 4/5
#             elif satuan_tujuan == 'K':
#                 hasil = celsius + 273.15
            
#             print(f'\nHasil: {suhu}°{satuan_awal} = {hasil:.2f}°{satuan_tujuan}\n')
            
#         except ValueError:
#             print('Error: Input harus berupa angka!\n')
#             continue
            
#         if input('Ulangi? (y/n): ').lower() != 'y':
#             print('Program selesai.')
#             break

# konversi_suhu()

