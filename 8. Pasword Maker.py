import random
import string

def generate_password(length = 12):
    #kumpulkan karakter
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    simbols = '!@#$%^&*'

    #gabungkan semua karakter
    all_char = lower + upper + digits + simbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(simbols)
    ]

    password += random.choices(all_char, k=length-4)

    #acak agar tidak berurutan
    random.shuffle(password)

    return ''.join(password)

panjang = input("Masukan panjang password (minimal 4) : ")

try:
    panjang = int(panjang)
    if panjang < 4:
        print("Panjang password minimal 4 krakter ")
    else:
        print("Memproses.......")
        hasil = generate_password(panjang)
        print(f'Hasil generate password = {hasil}')
except ValueError:
        print('Data yang dimasukan harus angka')

