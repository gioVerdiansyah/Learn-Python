# Duck Typing
# "If it walks like a duck, and it quacks like a duck then it must a duck"
# "Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek, kemungkinan besar ia adalah bebek".

# Konsep duck typing tidak berkaitan langsung dengan dynamic typing atau loosely typed, ini merupakan konsep yang lebih erat dengan materi kita kali ini, yaitu pemrograman berorientasi objek (object-oriented programming). Duck typing menjelaskan bahwa sebuah tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya.

# Class, object, dan method akan kita bahas secara mendalam pada materi kali ini. Kita hanya akan berkenalan terlebih dahulu secara umum sebelum spesifik membahasnya. Sebenarnya, Python ingin memberikan keleluasaan terhadap para developernya untuk tidak perlu mencemaskan tentang tipe atau kelas (class) dari sebuah objek (object), yang lebih penting adalah kemampuan melakukan operasinya (method).

# Mari kita ambil contoh, masih ingat dengan fungsi len()? len() merupakan fungsi yang bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. Bagaimana dengan tipe data numerik, seperti integer? Perhatikan kode di bawah ini.

i = 123
print(len(i))

# TypeError: object of type 'int' has no len()

# Pesan error tersebut menyatakan bahwa objek dengan tipe data "int" tidak memiliki len() yang tersedia, padahal seharusnya method tersebut diharapkan untuk ada. Python secara alami akan memeriksa jika object yang Anda buat memiliki method yang diharapkan atau tidak. Dalam contoh di atas, program menghasilkan error karena object tipe data 'int' tidak memiliki method len().