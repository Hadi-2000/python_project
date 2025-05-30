import time
import datetime
import os
import platform
import winsound  # Untuk Windows
import subprocess  # Untuk Linux/macOS

def tampilkan_notifikasi(judul, pesan):
    """Fungsi notifikasi multi-platform tanpa plyer"""
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {judul}: {pesan}")
    
    try:
        if platform.system() == "Windows":
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, pesan, judul, 0x40)
        elif platform.system() == "Darwin":  # macOS
            os.system(f'osascript -e \'display notification "{pesan}" with title "{judul}"\'')
        else:  # Linux
            subprocess.run(['notify-send', judul, pesan])
    except Exception as e:
        print(f"Gagal menampilkan notifikasi: {e}")

def bunyikan_alarm(panjang=False):
    """Fungsi alarm multi-platform"""
    try:
        if platform.system() == "Windows":
            if panjang:
                winsound.Beep(1000, 3000)
            else:
                winsound.Beep(1000, 1000)
        elif platform.system() == "Darwin":  # macOS
            if panjang:
                subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'])
                time.sleep(0.5)
                subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'])
            else:
                subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'])
        else:  # Linux
            if panjang:
                os.system('play -nq -t alsa synth 1 sine 1000')
                time.sleep(0.5)
                os.system('play -nq -t alsa synth 1 sine 1000')
            else:
                os.system('play -nq -t alsa synth 1 sine 1000')
    except:
        print("\a")  # Bunyi system default

def main():
    # Jadwal waktu (tetap sama)
    jadwal = {
        'kerja': [
            {'mulai': '08:00', 'selesai': '12:00', 'pesan': 'Waktunya Bekerja'},
            {'mulai': '13:00', 'selesai': '15:00', 'pesan': 'Waktunya Bekerja Kembali'}
        ],
        'istirahat': [
            {'mulai': '12:01', 'selesai': '12:59', 'pesan': 'Waktunya istirahat Siang'}
        ],
        'solat': [
            {'waktu': '05:30', 'nama': 'Subuh', 'pesan': 'Selamat menunaikan solat subuh'},
            {'waktu': '12:05', 'nama': 'Dzuhur', 'pesan': 'Selamat menunaikan solat dzuhur'},
            {'waktu': '13:15', 'nama': 'Asar', 'pesan': 'Selamat menunaikan solat asar'},
            {'waktu': '17:40', 'nama': 'Magrib', 'pesan': 'Selamat menunaikan solat magrib'},
            {'waktu': '18:45', 'nama': 'Isya', 'pesan': 'Selamat menunaikan solat isya'}
        ]
    }

    print("Sistem Manajemen Waktu Aktif (60m Kerja + 5m Istirahat)")
    print("Tekan Ctrl+C untuk menghentikan program\n")

    notifikasi_terakhir = {}
    sesi_kerja_count = 0
    dalam_sesi_kerja = False
    waktu_mulai_kerja = None

    try:
        while True:
            sekarang = datetime.datetime.now()
            time_now = sekarang.strftime("%H:%M")
            
            # Cek waktu solat terlebih dahulu (prioritas tinggi)
            for solat in jadwal['solat']:
                if time_now == solat['waktu']:
                    if notifikasi_terakhir.get(solat['nama']) != solat['waktu']:    
                        tampilkan_notifikasi("WAKTU SOLAT", solat['pesan'])
                        bunyikan_alarm(panjang=True)
                        notifikasi_terakhir[solat['nama']] = solat['waktu']
                        dalam_sesi_kerja = False  # Reset sesi kerja jika sedang solat
                    break
            else:
                # Cek jadwal kerja/istirahat utama
                for sesi in jadwal['kerja'] + jadwal['istirahat']:
                    if sesi['mulai'] <= time_now < sesi['selesai']:
                        if notifikasi_terakhir.get(sesi['pesan']) != sesi['mulai']:
                            tampilkan_notifikasi(sesi['pesan'].split(':')[0], sesi['pesan'])
                            bunyikan_alarm()
                            notifikasi_terakhir[sesi['pesan']] = sesi['mulai']
                            dalam_sesi_kerja = 'kerja' in sesi['pesan'].lower()
                            if dalam_sesi_kerja:
                                waktu_mulai_kerja = sekarang
                        break
                else:
                    # Sistem 60m kerja + 5m istirahat otomatis
                    if waktu_mulai_kerja is None:
                        waktu_mulai_kerja = sekarang
                        dalam_sesi_kerja = True
                        sesi_kerja_count += 1
                        tampilkan_notifikasi("MULAI KERJA", 
                                           f"Sesi kerja #{sesi_kerja_count} (60 menit)")
                        bunyikan_alarm()
                    
                    waktu_kerja_berlalu = (sekarang - waktu_mulai_kerja).total_seconds()
                    
                    if dalam_sesi_kerja and waktu_kerja_berlalu >= 60*60:  # 60 menit
                        dalam_sesi_kerja = False
                        waktu_istirahat_mulai = sekarang
                        tampilkan_notifikasi("WAKTU ISTIRAHAT", 
                                           "Istirahat 5 menit untuk peregangan")
                        bunyikan_alarm()
                    elif not dalam_sesi_kerja and (sekarang - waktu_istirahat_mulai).total_seconds() >= 5*60:  # 5 menit
                        dalam_sesi_kerja = True
                        waktu_mulai_kerja = sekarang
                        sesi_kerja_count += 1
                        tampilkan_notifikasi("MULAI KERJA", 
                                           f"Sesi kerja #{sesi_kerja_count} (60 menit)")
                        bunyikan_alarm()

            time.sleep(10)  # Cek setiap 10 detik

    except KeyboardInterrupt:
        print("\nProgram dihentikan")

if __name__ == "__main__":
    main()