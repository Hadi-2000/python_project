print('Pengidentifikasi angka sederhana')
while True:
    try:
        angka = float(input('Masukan angka = ').strip())

        if angka.is_integer():
            angka = int(angka)
    except ValueError:
        print('Error: Input harus berupa angka (int/float)!')
        continue

    if isinstance(angka, (int,float)):
        #ganjil genap
        if angka % 2 == 0 :
            print(f'Angka {angka} adalah bilangan Genap.')
        else:
            print(f'Angka {angka} adalah bilangan Ganjil.')
        
        #Positif Negatif
        if angka > 0 :
            print(f'Angka {angka} adalah bilangan Positif.')
        elif angka < 0:
            print(f'Angka {angka} adalah bilangan Negatif.')

        #Bulat Desimal
        if isinstance(angka, int) :
            print(f'Angka {angka} adalah bilangan Bulat.')
        elif isinstance(angka, float):
            print(f'Angka {angka} adalah bilangan Pecahan/Desimal.')
        
        #bilangan prima
        if angka > 1:
            for i in range (2, int(angka**0.5) + 1):
                if angka % i == 0:
                    break
                
                print(f'Angka {angka} adalah bilangan Prima.')
                break
    else:
        print('Data yang dimasukan bukan angka.')
    if not angka:
        print('Tolong data masukan diisi dan tidak boleh kosong.')
    f = 0
    if f == 0:
        pilihan = input('Apakah anda ingin mencoba lagi ? (Y/N)').upper()
        if pilihan == 'Y':
            print('=====================================================================')
        elif pilihan == 'N':
            print('Aplikasi akan dimatikan')
            print('=====================================================================')
            exit()
        else:
            print('Data yang dimasukan tidak terdefinisi. Silahkan pilih Y atau N.')
    
