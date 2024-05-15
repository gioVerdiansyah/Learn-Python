# Module adalah sebuah file berisi kode Python dan di dalamnya terdapat fungsi, kelas, dan sebagainya.

# Sebab setiap file berekstensi .py dapat direferensikan sebagai modul, Anda bisa melakukan impor file dari satu file ke yang lainnya. Layaknya ketika Anda menggunakan library, modul, dan sebagainya.

# Contoh me import
import Utilities

# Contoh penggunaannya
print(Utilities.increase(10,20))

# Import dengan spesifik
from Utilities import pi

print(pi)


# Alias
import Utilities as util
print(util.increase(12,90))