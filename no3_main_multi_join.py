import threading
import time

def cetak_angka():
    for i in range(5):
        print("Angka:", i)
        time.sleep(1)

def cetak_huruf():
    for huruf in ['A', 'B', 'C', 'D', 'E']:
        print("Huruf:", huruf)
        time.sleep(1)

# Membuat dua thread
t1 = threading.Thread(target=cetak_angka)
t2 = threading.Thread(target=cetak_huruf)

# Menjalankan thread
t1.start()
t2.start()

# Tunggu kedua thread selesai
t1.join()
t2.join()

print("Selesai semua!")

# Kalau kamu jalankan kode di atas, kamu akan lihat angka dan huruf muncul berselang-seling,
# karena dua fungsi jalan bersamaan.
