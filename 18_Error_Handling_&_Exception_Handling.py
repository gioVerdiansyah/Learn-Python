# Penanganan Kesalahan (Error Handling and Exception Handling)
# Saat Anda membuat program, sering kali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya.

# Kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors).
# Pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors).



# Kesalahan Sintaks (Syntax Errors)
# Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda. Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan.

# Salah satu tipe kesalahan sintaks yang sering ditemui adalah kesalahan indentasi (IndentationError). Berikut contoh kodenya.

# if 9>10:
# print("Hello World!")

#   File "D:\Document\Learn Python\18_Error_Handling_&_Exception_Handling.py", line 15
#     print("Hello World!")
#     ^
# IndentationError: expected an indented block after 'if' statement on line 14

# Error di atas memiliki struktur, kurang lebih struktur error seperti ini:
# File "<file path>", line <nomor baris>
#   <baris kode dengan kesalahan>
#               ^
# <tipe kesalahan>: <pesan kesalahan>


# Penanganan error
# Kita bisa lakukan penanganan terhadap pengecualian tersebut dengan menggunakan pernyataan try-except. Berikut strukturnya.
# try:
    # Blok kode yang kemungkinan muncul error
# except:
    # Penanganan jika blok pada try terjadi kesalahan

# Contoh penggunaan
x = 0
try:
    print(1/x)
except ZeroDivisionError:
    print("Anda tidak dapat membangi angka dengan nilai 0")


# Struktur lengkap penganagan error ataupun exception:
# try:
    # Blok kode yang kemungkinan muncul error
# except:
    # Penanganan jika blok pada try terjadi kesalahan
# else:
    # pernyataan di operasikan jika tidak ada pengecualian
# finally:
    # pernyataan di operasiian setelah semua pernyataan di operasikan

# Contoh
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

# rata-rata adalah 1.0
# Kode ini dieksekusi jika tidak ada exception.
# Kode ini dieksekusi terlepas dari ada atau tidaknya exception.



# Rasie Exception
# Membuat error / exception secara di sengaja
# raise digunakan bersamaan dengan if-else statement

val = -1
if val < 0:
    raise ValueError("Negative number is not allowed!")
else:
    for i in range(val):
        print(i + 1)

# Traceback (most recent call last):
#   File "D:\Document\Learn Python\18_Error_Handling_&_Exception_Handling.py", line 80, in <module>
#     raise ValueError("Negative number is not allowed!")
# ValueError: Negative number is not allowed!