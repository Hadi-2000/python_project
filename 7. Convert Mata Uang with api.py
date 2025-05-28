import os
from dotenv import load_dotenv
import requests

load_dotenv()

def convert_mata_uang(jumlah, awal, akhir):
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print('Error: Api Key tidak ditemukan. pastikan file .env beserta isinya sudah dibuat.')
        return None
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{awal}/{akhir}/{jumlah}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                "Hasil" : data["conversion_result"],
                "Rate" : data["conversion_rate"]
            }
        else:
            print(f"Error: {data.get('error-type', 'Unknown error')}")
            return None
    except Exception as e:
        print(f'Error {e}')
        return None

if __name__ == "__main__":
    print('\n======Konversi Mata Uang======')
    print('Mata Uang yang disediakan = ')
    print('IDR, USD, AEF, AFN, ALL, AMD, AUD, BGN, CAD, CHF, CNY, EGP, EUR, GBP')
    try:
        jumlah = float(input('Masukan jumlah nominal uang : '))
        awal = input('Masukan mata uang awal :').strip().upper()
        akhir = input('Masukan mata uang akhir :').strip().upper()
        hasil = convert_mata_uang(jumlah, awal, akhir)
            
        if hasil:
            print(f"\n🔄 Hasil Konversi:")
            print(f"{jumlah} {awal} = {hasil['Hasil']} {akhir}")
            print(f"Kurs 1 {awal} = {hasil['Rate']} {akhir}")
        else:
            print("\nGagal melakukan konversi mata uang, cek data yang dimasukan benar")
    except ValueError:
        print('Error: Jumlah harus angka.')
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")