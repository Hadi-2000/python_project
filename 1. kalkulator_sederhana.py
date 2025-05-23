print('===== Kalkulator Sederhana =====')
print('9   8   7  C')
print('6   5   4  -')
print('3   2   1  :')
print('=   0   +  x  OFF')

hasil = 0
i = 0
angka1 = int(input('Masukan angka : '))

while i == 0:
    operator = input('Masukan operasi hitung : ')
    

    if(operator == '+' or operator == '-' or operator == ':' or operator.upper() == 'X'):
        angka2 = int(input('Masukan angka : '))
        
        if(operator == '+'):
            hasil = angka1 + angka2
            print(f'Hasil = {hasil}')
            angka1 = hasil
        elif(operator == '-'):
            hasil = angka1 - angka2
            print(f'Hasil = {hasil}')
            angka1 = hasil
        elif(operator == ':'):
            hasil = angka1 / angka2
            print(f'Hasil = {hasil}')
            angka1 = hasil
        elif(operator == 'X' or operator == 'x'):
            hasil = angka1 * angka2
            print(f'Hasil = {hasil}')
            angka1 = hasil
    elif(operator.upper() == 'C'):
        print('============================================')
        angka1 = 0
        angka1 = int(input('Masukan angka : '))
    elif(operator.upper() == 'OFF'):
        print('============================================')
        print('Aplikasi telah dimatikan')
        print('============================================')
        angka1 = 0
        i = 1
    else:
        print('Operator tidak teridentifikasi')

  
