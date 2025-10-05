import threading

counter = 0
lock = threading.Lock()  # buat objek lock

def tambah():
    global counter
    for _ in range(5000000):
        with lock:      # hanya satu thread yang boleh masuk bagian ini
            counter += 1

t1 = threading.Thread(target=tambah)
t2 = threading.Thread(target=tambah)

t1.start()
t2.start()
t1.join()
t2.join()

print("Hasil akhir:", counter)

# Sekarang kita masuk ke contoh penggunaan Lock dalam threading Python.
# Lock digunakan untuk menghindari tabrakan (race condition) saat beberapa thread mengakses data yang sama.