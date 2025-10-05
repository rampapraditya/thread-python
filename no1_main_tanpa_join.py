import threading
import time

def cetak():
    for i in range(5):
        print("Thread jalan:", i)
        time.sleep(1)

t = threading.Thread(target=cetak)
t.start()

print("Program Utama Dijalankan")

# tanpa join
# thread.join() digunakan untuk menunggu thread selesai sebelum program lanjut ke baris berikutnya.
# Kalau tidak ada .join(), program utama bisa selesai duluan sebelum thread lain sempat menyelesaikan tugasnya.