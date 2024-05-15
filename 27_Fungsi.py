# fungsi dalam pemrograman adalah blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil. Dalam Python, fungsi terbagi menjadi dua jenis.
# Dalam Python, fungsi terbagi menjadi dua jenis.

# Built-in Functions
# Built-in functions atau dalam bahasa Indonesia berarti fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan fungsi-fungsi inti dan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.
# User-defined Functions
# User-defined functions atau dalam bahasa Indonesia berarti fungsi yang didefinisikan pengguna adalah jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang.

# Nama          Definisi                                            Contoh
# Fungsi        Blok kode yang dapat digunakan kembali              print(), len(), searches_square()
# Built-in      Kumpulan fungsi yang sudah terintegrasi             print(), len(), range()
# Function      dengan bahasa pemrograman Python
# User-defined  Jenis fungsi yang kita definisikan sendiri          searches_square()
# Modul         File berisi kode Python berupa fungsi,kelas         main.py, var.py, dan lain sebagainya
# Package       Sebuah direktori berisi satu atau lebih             NumPy, Pandas
#               modul yang terkait dan saling berhubungan.
# Library       Koleksi dari banyaknya modul dan paket yang         Matplotlib, TensorFlow, Beautiful Soup
#               saling terkait dan dapat digunakan berulang kali.

# Membuat fungsi
def searches_square(width, height):
    return width * height


# menggunakannya
print(searches_square(5, 10))  # 50


# Docstring
# Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.

def mencari_luas_persegi_panjang(panjang, lebar):
    """

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


# Argumen dan Parameter

# a dan b adalah parameter
def my_func(a,b):
    print(a*b)

# a dan b dibawah adalah argumen yg harus di isi untuk fungsi my_func
my_func(10, 12)


# Argumen
# positional-or-keyword
def say(name, message):
    return "Hello " + name + "! " + message

print(say("Verdi", "Keep smile:)"))
print(say(message="you can do it!", name="Verdi"))

# Positional only
def increase(a, b, /):
    return a + b

print(increase(10, 5))
# print(increase(b=3, a=10))
# increase() got some positional-only arguments passed as keyword arguments: 'a, b'

# Keywoard only
def decrease(*, a, b):
    return a - b

print(decrease(b=5, a=12))
# print(decrease(12,13))
# decrease() takes 0 positional arguments but 2 were given


# Variadic-positional
def calc(*args):
    print(type(args)) # <class 'tuple'>
    return sum(args)

print(calc(1,2,3,4,5,6,7,8,9,10))


# Variadic keyword parameter
def print_info(**kwargs):
    text = ""
    for key,value in kwargs.items():
        text += key + ": " + value + "\n"
    return text

print(print_info(name="Verdi", age="17", hobby="Coding"))
# name: Verdi
# age: 17
# hobby: Coding




# Fungsi Anonim (Lambda Expression)
# Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya.
# Struktur
# name = lambda args : ret_val

# Contoh
add = lambda a,b : a+b

print(add(12,15))