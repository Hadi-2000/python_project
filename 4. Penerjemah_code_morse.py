def text_to_morse(text):
    morse_kode_list = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            ' ': '/'  # Spasi antar kata
        }
    morse_kode = []

    for char in text.upper() :
        if char in morse_kode_list:
            morse_kode.append(morse_kode_list[char])
        else:
            print(f'Data "{char}" yang dimasukan tidak terdefinisi')
            return None
    return ''.join(morse_kode)
            
def morse_to_text(text):
    original_kode = {
        '.-' : 'A', '-...' : 'B','-.-.' : 'C','-..' : 'D','.' : 'E','..-.' : 'F',
        '--.' : 'G','....' : 'H' ,'..' : 'I', '.---' : 'J','-.-' : 'K','.-..' : 'L',
        '--' : 'M', '-.' : 'N', '---' : 'O', '.--.' : 'P','--.-' : 'Q','.-.' : 'R',
        '...' : 'S','-' : 'T','..-' :'U','...-' : 'V','.--' : 'W','-..-' : 'X',
        '-.--' : 'Y','--..' : 'Z',
        '.----' : '1','..---' : '2','...--':'3','....-':'4','.....':'5',
        '-....':'6','--...':'7', '---..':'8','----.':'9', '-----':'0',
        '/': ' '
    }
    morse_kode = []

    for code in text.split() :
        if code in original_kode:
            morse_kode.append(original_kode[code])
        else:
            print(f'Data "{code}" yang dimasukan tidak terdefinisi')
            return None
    return ''.join(morse_kode)
     
print('===================================')
print('Jasa penerjemah yang disediakan :')
print('1. huruh/kalimat jadi kode morse.')
print('2. kode morse jadi huruf/kalimat.')
print('3. keluar')
print('==================================')
while True:
    try:
        jasa = input('Mau memakai jasa yang mana :(1/2/3)?')

        if(jasa == '1'):
            awal = input('Masukan kalimat/huruf : ')
            print('Proses sedang berlangsung mengubah jadi kode morse')
            morse_result = text_to_morse(awal)
            if morse_result is not None:
                print(f'Hasil = {morse_result}')
        elif(jasa == '2'):
            awal = input('Masukan morse : ')
            print('Proses sedang berlangsung mengubah jadi huruf/kalimat')
            morse_result = morse_to_text(awal)
            if morse_result is not None:
                    print(f'Hasil = {morse_result}')
        elif(jasa == '3'):
            print('Aplikasi dimatikan')
            print('===============================')
            break
        else:
            print('Pilihan tidak valid! Masukkan 1, 2, atau 3')
    except KeyboardInterrupt:
            print('\nAplikasi dihentikan oleh pengguna')
            break
