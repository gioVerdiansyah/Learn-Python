# One-liner
# membuat sebuah kode hanya dalam satu baris saja atau berupa single statement. Konsep ini dikenal sebagai one-liner.
#
# One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris. One-liner adalah salah satu keunggulan dalam Python yang susah untuk diimplementasikan bagi beberapa bahasa pemrograman lainnya.
#
# Tujuan dari one-liner ini adalah membuat satu baris kode yang singkat dan jelas. Perlu diingat bahwa tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas.

# Contoh khasus:
x = 1
y = 2

temp = x
x = y
y = temp

print(f"Nilai X: {x}")
print(f"Nilai Y: {y}")

# Langkah seperti ini:
# X -> temp
# Y -> X
# temp -> Y


# Dengan One-liner
a = 1
b = 2

a,b = b,a
print(f"Nilai A: {a}")
print(f"Nilai B: {b}")

# Pada kode di atas, Anda seolah-olah menginisialisasikan ulang variabel x dengan nilai variabel y di sebelah kanan. Anda juga menginisialisasikan ulang variabel y dengan nilai variabel x yang ada di sebelah kanan. Sederhana, bukan? Dengan menginisialisasikan ulang variabel masing-masing, nilai tersebut pada akhirnya bisa saling bertukar.