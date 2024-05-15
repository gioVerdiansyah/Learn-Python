import array
# Fundamental Array
# Python tidak memiliki tipe data array yang sering digunakan dalam bahasa pemrograman lain. Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array.
#
# Perbedaan yang menonjol adalah cara array menyimpan nilai sangat berbeda dengan list. Pada array, nilai di dalamnya harus memiliki tipe data yang sama. Namun, pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama.

# array bukan hanya sebuah tipe data, melainkan salah satu tipe struktur data berjenis linear.
# Struktur data adalah cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien. Dengan adanya struktur data, setiap data yang disimpan memiliki hubungan satu sama lain dan kita dapat beroperasi dengan setiap data tersebut.

# Dari sini, kita harus bisa menyamakan persepsi bahwa array dan list merupakan hal yang berbeda dalam Python. Kendati demikian, Anda bisa menggunakan list sebagai array dalam Python.

my_list = [1,2,3,4,5]
print(my_list) # [1,2,3,4,5]

# Jika Anda benar-benar ingin menggunakan array, Anda pun bisa mendeklarasikan array dalam Python dengan menggunakan library atau modul Python. Salah satunya modul bernama "array".

arry = array.array('i', [1,2,3,4,5])
print(arry) # array('i', [1, 2, 3, 4, 5])
print(type(arry)) # <class 'array.array'>

# Pada contoh di atas, kita membuat array bertipe integer dengan menyatakan "i" sebelum array. Sekarang, coba Anda ubah nilai array "[1, 2, 3, 4, 5]" menjadi "[1, 2, 3, 4, 5, 'Dicoding']". Apa yang terjadi? Jika yang terjadi adalah error, hal ini disebabkan karena nilai atau elemen dalam array harus bertipe sama atau identik.
# Struktur data linear adalah jenis struktur data yang elemen-elemen nilai di dalamnya disusun secara berurutan atau linear.
# Struktur data non-linear merupakan jenis struktur data yang elemen-elemen nilai di dalamnya tidak disusun secara linear.

# Array adalah salah satu jenis dari struktur data linear. Dalam konteks ini, array terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear.
