# Operator Aritmatika
# Jenis pertama adalah operator untuk melakukan operasi aritmetika. Perhatikan tabel di bawah ini untuk memahami contoh penerapan operator aritmetika. Asumsikan x bernilai 10 dan y bernilai 3.
# Operator              Deskripsi                                                   Contoh
# Penjumlahan (+)       Menambahkan nilai dari kedua operan.                        x + y = 13
# Pengurangan           Mengurangi nilai dari kedua operan.                         x - y = 7
# Perkalian (*)         Mengalikan nilai dari kedua operan.                         x * y = 30
# Pembagian Bulat (//)  Membagi nilai dari kedua operan.                            x // y = 3
#                       Jika operan integer, hasil operasi adalah bilangan bulat.
# Pembagian Riil (/)    Membagi nilai dari kedua operan. Jika operan adalah float,  x / y = 3.3
#                       hasil operasi adalah bilangan riil.
# Modulo (%)            Sisa hasil pembagian nilai dari dua operan.                 x % y = 1
# Pangkat (**)          Memangkatkan nilai dari dua operan.                         x ** y = 1000

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)


# Operator Relasional
# Operator relasional merupakan operator perbandingan antara dua operan yang berupa integer, float, string, ataupun boolean. Hasil akhir dari operator ini adalah nilai bertipe boolean. Perhatikan tabel di bawah untuk memahami contoh penerapan operator relasional. Asumsikan kedua variabel bertipe numerik atau float dengan x bernilai 5 dan y bernilai 10.
# Operator                          Deskripsi                                                           Contoh
# Sama dengan (==)                  Menghasilkan True, jika kedua operan bernilai sama.                 x == y (False)
# Tidak Sama dengan (!=)            Menghasilkan True, jika kedua operan tidak bernilai sama.           x != y (True)
# Lebih Besar dari (>)              Menghasilkan True, jika operan kiri lebih besar dari operan kanan.  x > y (False)
# Kurang dari (<)                   Menghasilkan True, jika operan kanan lebih besar dari operan kiri.  x < y (True)
# Lebih Besar dari Sama dengan (>=) Menghasilkan True, jika operan kiri lebih besar atau sama dengan    x >= y (False)
#                                   operan kanan.
# Kurang dari Sama dengan (<=)      Menghasilkan True, jika operan kanan lebih besar atau sama dengan   x <= y (True)
#                                   operan kiri.

x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Operator relasional jika String
# Operator                  Deskripsi                                                   Contoh
# Sama dengan (==)          Menghasilkan True, jika kedua string memiliki nilai yang    x == y (False)
#                           identik/sama persis.
# Tidak Sama dengan (!=)    Menghasilkan True, jika kedua string memiliki nilai yang    x != y (True)
#                           tidak sama.
# Lebih Besar dari (>)      Menghasilkan True, jika huruf pertama pada string pertama   x > y (False)
#                           memiliki nilai unicode dengan urutan yang lebih tinggi
#                           dibandingkan huruf pertama pada string kedua.
# Kurang dari (<)           Menghasilkan True, jika huruf pertama pada string pertama   x < y (True)
#                           memiliki nilai unicode dengan urutan yang lebih rendah
#                           dibandingkan huruf pertama pada string kedua.
# Lebih Besar dari Sama     Menghasilkan True, jika huruf pertama pada string pertama   x >= (False)
# dengan (>=)               memiliki nilai unicode dengan urutan yang lebih tinggi atau
#                           sama dibandingkan huruf pertama pada string kedua.
# Kurang dari Sama          Menghasilkan True, jika huruf pertama pada string pertama   x <= y (True)
# dengan (<=)               memiliki nilai unicode dengan urutan yang lebih rendah atau
#                           sama dibandingkan huruf pertama pada string kedua.


x = "Dicoding"
y = "Indonesia"
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Operator Logika
# Operator logika merupakan jenis operator untuk melakukan operasi logika dengan kedua operannya bertipe boolean. Hasil akhir dari operasi ini adalah nilai bertipe boolean. Perhatikan kode di bawah ini untuk memahami contoh penerapannya, asumsikan bahwa A bernilai True dan B bernilai False.
# Operator          Deskripsi                                   Contoh
# AND (&)           True jika kedua operan bernilai True        A and B (False)
# OR (|)            True jika salah satu operan bernilai True   A or B (True)
# NOT               Membalikan nilai operan                     not A (False)

A = True
B = False
print(A and B)
print(A or B)
print(not A)

# Operator Assignment
# Operator selanjutnya adalah assignment. Operator ini bertujuan untuk melakukan proses assignment atau pemberian nilai pada suatu variabel dengan nilai tetap. Perhatikan tabel di bawah ini untuk memahami contoh penerapan operator assignment. Asumsikan x bernilai 10 dan y bernilai 5.
# Operator      Asalnya         Contoh
# +=            x = x + y       x += y (15)
# -=            x = x - y       x -= (5)
# *=            x = x * y       x *= (50)
# /=            x = x / y       x /= y (2)
# %=            x = x % y       x %= y (0)

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)
