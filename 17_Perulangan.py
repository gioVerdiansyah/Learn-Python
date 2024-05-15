# Perulangan
# Sesuatu yang dilakukan secara berulang
# Contoh khasus:
# print angka 1 samapai 10


# for
# For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.
# Format perulangan for
# for <var> in <iterable>:
    # <statement(s)>

# <iterable>
# merupakan segala object dalam Python yang dapat diiterasi seperti list, tuple, hingga string
# <var>
# merupakan variabel yang akan mengambil elemen berikutnya dari <iterable> setiap kali iterasi berjalan.

# contoh:
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i) # 1 - 10

# fungsi range
# "range()" adalah fungsi bawaan dalam Python yang akan menghasilkan urutan bilangan dimulai dari indeks ke-0.
# Sintaksis umum dari fungsi "range()" sebagai berikut.
# range(start, stop, step)

# contoh:
for i in range(10):
    print(i) # 0 - 9

for i in range(1, 10, 2):
    print(i) # 1 3 5 7 9


# while
# While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

# Format dari perulangan while sebagai berikut.
# while kondisi:
    # Blok eksekusi selama kondisi bernilai True

# contoh:
count = 1
while count <= 5:
    print(count) # 1 - 5
    count += 1

# Infinity loop
# Inifity loop terjadi ketika kondisi pada perulangan selalu terpenuhi sehingga program melakukan perulangan tanpa henti
# Contoh:
# white count <= 5:
    # print(i)

# Tanpa increment maka kondisi akan selalu terpenuhi ini mengakibatkan infinity loop


# for bersarang
# Perulangan dalam perulangan atau di kenal nested loop
# Format nested loop:
# for i in range(1, 3):
    # for j in range (1, 3):

# Contoh:
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)

# 1, 1
# 1, 2
# 1, 3
# 1, 4
# 2, 1
# 2, 2
# 2, 3
# 2, 4
# 3, 1
# 3, 2
# 3, 3
# 4, 4


# Kontrol perulangan
# Mengontrol perulangan seperti menghentikan atau melanjutkan

# break
# Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.

for i in range(2):
    print(i)
    for j in range(5):
        print(j)
        if j == 1:
            break # Jika perulangan j = 1 maka berhentikan perulangannya dan ulang lagi dari for pertama sampai for pertama menyelesaikan kondisinya

# Alhasil j tidak sampai 0 - 5 melainkan 0 - 1 saja

# Contoh lain
for word in "Sofyan Gio":
    if word == ' ':
        break
    print(word) # hanya sampai Sofyan saja


# Continue
# Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.

for word in "Sofyan Gio":
    if word == ' ':
        continue
    print(word)


# Alhasil semua huruf tercetak kecuali spasi, seperti di lewati


# else setelah for
# Seperti jalan keluar for jika for selesai

numbers = [1,2,3,4]
for i in numbers:
    if i == 5:
        print("Angka 5 ditemukan, program berhenti!")
        break
else:
    print("Angka 5 tidak ditemukan")


# else setelah while
# Perbedaannya adalah blok else akan di eksekusi setelah kondisi pada while sudah terpenuhi

counter = 1
while counter <= 3:
    print(f"{counter}X")
    counter += 1
else:
    print(f"Program while selesai karena {counter} >= 3 (True)")

# Jika selesai menggunakan break:
n = 10
while n >= 0:
    n -= 1
    if n == 5:
        break
    print(n)
else:
    print("While selesai karena break")

# statemennt else tidak tercetak karena kondisi pada while masih terpenuhi


# pass
# Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
# Contoh:

x = 10
if x >= 5:
    pass
else:
    print("x <= 10")

# Program di atas tidak menampilkan apa pun karena jika kondisi terpenuhi, program tidak akan melakukan apa pun.


# List Comprehension
# Masih terkait perulangan, terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.

# Contoh khasus:
num = [1,2,3,4,5]
rank = []
for i in num:
    rank.append(i**2)
print(rank) # [1, 4, 9, 16, 25]

# Solusi singkat:
ranks = [m**2 for m in num]
print(ranks) # [1, 4, 9, 16, 25]