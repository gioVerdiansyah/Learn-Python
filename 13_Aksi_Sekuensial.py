# Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara sekuensial. Apa maksudnya? Kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. Aksi sekuensial sendiri memiliki makna sebagai sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya.
#
# Dengan kata lain, program yang Anda bangun haruslah memiliki awal dan akhir. Jadi, ketika program tersebut dijalankan, bisa diketahui waktu berakhirnya. Simak kode di bawah ini untuk melihat implementasinya.

print("Selamat datang di program Python!\n")
print("Silahkan masukkan data diri Anda:")

nama = input("Masukkan nama Anda: ")
thn_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2024 - int(thn_lahir)

print(f"Selamat datang {nama} dalam program Python, per 2024 umur Anda adalah {umur} tahun.")
print("Terimakasih telah menggunakan program Python")

# Keseluruhan kode tersebut menggambarkan bahwa program akan dijalankan berdasarkan urutan perintahnya. Perlu diperhatikan bahwa terdapat program yang akan berubah hasilnya jika urutan baris instruksinya diubah. Ada juga program yang hasilnya TIDAK akan berubah jika urutan baris instruksinya diubah.

a = 9
b = 6
result = a + b

print(result) # 15

# Meski saya ubah urutan nilai pada variabel a dan b maka hasil nya akan sama saja
# misal a = 6 b = 9 maka akan sama saja


# Namun bagaimana dengan urutan instruksi yang mengubah hasil?
print(a**2) # 81
print(a//3) # 3

print(a//3) # 3
print(a**2) # 81

# Kode di atas merupakan program yang sama dengan kode sebelumnya. Namun, hasil yang didapat berbeda karena Anda mengubah urutan sintaks "print()".