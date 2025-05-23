import random

print('Selamat datang di Acak Dadu sederhana')
i = 0
hasil = 0

while i == 0:
    aksi = input('Apakah anda ingin mengacak dadu : (Y/N)')
    
    if(aksi.upper() == 'Y'):
        hasil = random.randint(0,6)
        print(f'Hasil acakan dadu = {hasil}')
    elif(aksi.upper() == 'N'):
        print('=========================================')
        print('Aplikasi dimatikan')
        print('=========================================')
        i = 1
    else:
        print('Data yang dimasukan tidak terdefinisi')
