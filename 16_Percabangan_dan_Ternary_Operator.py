# Percabangan dan Ternary Operators
# Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir. Pada materi sebelumnya, Anda telah mempelajari aksi sekuensial. Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.

# Percabangan
# Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else).
#
# Misalnya dalam keadaan seperti berikut.
#
# Jika Anda tidak menyelesaikan kelas Memulai Pemrograman dengan Python, maka Anda tidak lulus dari kelas Memulai Pemrograman dengan Python.
# Jika jumlah variabel nama kurang dari dua, maka variabel tersebut tidak memenuhi kriteria kondisi.

# Contoh:
# Ibu kepasar -> Apakah daging ada?
# Jika ada -> Membeli daging
# Jika tidak add maka -> Membeli tempe

stock = "Daging ayam"

if stock == "Daging ayam":
    print("Ibu membeli daging ayam")
else:
    print("Ibu membeli tempe")


# if
# If adalah statement Python yang akan mengecek nilai apakah memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.
# if kondisi:
    #block yang akan di eksekusi jika true

score = 100
if score >= 90:
    print("Grade nilai Anda adalah A")


# Python menganggap setiap nilai kosong (zero) dan null sebagai False. Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True.
val = ""
if val:
    print("Benar") # Tidak akan dijalankan
# Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.

# 1.) Nilai yang sudah didefinisikan bernilai salah: None dan False.
# 2.) Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
# 3.) Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).

# if versi one-liner
if score == 100: print("Nilai sempurna!")



# else
# Else adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if statement bernilai false. Maksudnya adalah program akan menjalani blok kode if terlebih dahulu dan jika hasilnya adalah false, program akan menjalankan else statement sebagai jalan keluar atau kondisi terakhir.
# if kondisi:
    # Blok eksekusi jika True
# else:
    # Block eksekusi jika False

# Contoh
my_height = 145

if my_height >= 160:
    print("Anda di perbolehkan naik Roler coaster")
else:
    print("Anda tidak di perbolehkan naik Roler coaster")



# Elif
# Elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. Elif statement berada pada posisi setelah if. Anda dapat menambahkan elif statement lebih dari satu karena tidak dibatasi dan opsional.
# if kondisi1:
    # Blok jika kondisi1 True
# elif kondisi2:
    # Blok jika kondisi2 True
# else:
    # Blok jika semua kondisi False


point = 75

if point >= 80:
    print("Anda mendapatkan Grade A")
elif point >= 70:
    print("Anda mendapatkan Grade B")
elif point >= 65:
    print("Anda mendapatkan Grade C")
elif point >= 60:
    print("Anda mendapatkan Grade D")
else:
    print("Anda mendapatkan Grade E")


# Ternary Operators
# Ternary operators termasuk conditional expressions pada Python. Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else.

# Contoh Ilustrasi

# If-Else statement
# if kondisi:
    # blok_jika_benar
# else:
    # blok_jika_salah

# Ternary Operator
# blok_jika_benar if kondisi else blok_jika_salah

passed = True

print("Selamat Anda lulus!") if passed else print("Coba lagi tahun depan")

# Ternary dengan tuple
# (block_jika_salah, blok_jika_benar)[kondisi]

graduation = ("Silahkan coba lagi tahun depan", "Selamat atas kelulusannya!")[passed]
print(graduation)