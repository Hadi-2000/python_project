import random

print('====================================')
print('    Game Tebak Angka Sederhana      ')
print('====================================')

while True:
    pilihan = input('Apakah kamu ingin memainkan permainan ini (Y/N)')
    if(pilihan.upper() == 'Y'):
        percobaan = 0
        angka = random.randint(1,10)
        print('Pilihlah angka 1-10, dan tebak angka dari komputer maksimal 3 kali tebakan')
        
        while percobaan < 3:
            try:
                tebak = int(input('Angka yang kamu tebak adalah : '))
            except ValueError:
                print('Harap masukkan angka yang valid!')
                continue

            percobaan += 1
            
            if(tebak == angka):
                print('Tebakan anda benar')
                keluar = input('Apakah anda ingin keluar (Y/N)').upper()
                
                if(keluar == 'Y'):
                    exit()
                elif(keluar == 'N'):
                    break
                else:
                    print('Inputan tidak terdefinisi')
                    print('==========================================')
                    keluar = input('Apakah anda ingin keluar (Y/N)')
            elif(tebak != angka):
                sisa = 3 - percobaan
                print('Tebakan anda salah')
                print(f'Tersisa {sisa} percobaan lagi')
                if(percobaan != 3):
                    if(angka < tebak):
                        print('Angka lebih kecil dari yang ditebak')
                    elif(angka > tebak):
                        print('Angka lebih besar dari yang ditebak')
                    else:
                        print('Data yang diinput tidak terdefinisi')

                    print('===============================')
                elif(percobaan == 3 ):
                    print('Anda telah gagal menebak sebanyak 3 kali')
                    print(f'Angka yang benar adalah: {angka}')
                    print('===============================================')
                    print('               DEFEAT'                          )
                    print('===============================================')
            else:
                print('Data tidak terdefinisi')
    elif(pilihan.upper() == 'N'):
        print('Aplikasi ini telah dimatikan')
        print('============================================')
    else:
        print('Data yang dimasukan tidak terdefinisi')
        print('============================================')

