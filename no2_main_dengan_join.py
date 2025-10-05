import threading
import time

def cetak():
    for i in range(5):
        print("Thread jalan:", i)
        time.sleep(1)

t = threading.Thread(target=cetak)
t.start()

t.join()  # menunggu thread selesai
print("Selesai program utama!")
