# Fundamental Matriks
# Sebenarnya, array adalah jenis struktur data 1 dimensi yang menyimpan semua datanya secara linear. Pada materi ini, kita akan mempelajari jenis array 2 dimensi, yakni matriks.
# Matriks pada matematika merupakan himpunan yang terdiri dari bilangan atau elemen berdasarkan baris dan kolom. Dalam matematika, struktur matriks sebagai berikut.
# Dalam matematika, penamaan baris dan kolom dibuat secara berurutan, baris ke-1 dimulai dari atas hingga ke bawah dan kolom ke-1 dimulai dari kiri ke kanan.
import sys

import numpy

# Contoh matriks dalam matematika beragam jenisnya, beberapa di antaranya sebagai berikut.
# 1. Matriks Pengukuran
# Matriks pengukuran adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan termasuk bilangan real atau tipe data float.

# 2. Matriks Satuan
# Selanjutnya adalah matriks satuan dengan elemen bernilai hanya 0 atau 1. Setiap elemen matriks ini bertipe data integer.


# Sementara itu dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list.
# Dalam gambar di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikannya dengan nested list atau list di dalam list. Perhatikan lebih baik,  pada gambar tersebut terdapat dua kurung siku "[]" dan kurung siku pertama adalah list yang membungkus tiga list di dalamnya, yakni "[1, 2, 3], [4, 5, 6], [7, 8, 9]".
#
# Matriks dalam pemrograman dapat kita simpulkan sebagai berikut.
#
# 1. Matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom.
# 2. Setiap elemen matriks dapat diakses melalui metode indexing jika kedua indeks telah diketahui.
# 3. Elemen matriks dideklarasikan memiliki tipe homogen yang artinya elemen tersebut harus mempunyai tipe data yang sama. Jika elemen tersebut adalah bilangan real, seluruh elemen lainnya pun adalah bilangan real. Walaupun dalam list Python Anda dapat membuat matriks dengan tipe data berbeda, alangkah lebih baik jika tetap mengikuti aturan ini.


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Namun, perlu diingat bahwa mendeklarasikan matriks menggunakan list sangat memakan banyak memori. Masih ingatkah Anda dengan materi array yang menyatakan bahwa setiap nilai atau elemen dalam list akan disimpan pada masing-masing tempat memori? Hal ini berlaku juga pada matriks.
#
# Jika kita membuat matriks dengan 100 kolom dan 100 baris akan menghasilkan 10.000 elemen integer dalam matriks tersebut dan menggunakan 10.000 penyimpanan untuk menampung semua elemen integer.
#
# Oleh karena itu, menggunakan nested list sebagai matriks dianggap cara yang cukup praktis, tetapi tidak efektif dalam mengelola penyimpanan memori. Jika Anda ingin membuat matriks dengan jumlah elemen yang besar, programmer Python biasanya menggunakan library tambahan seperti NumPy untuk melakukan tugasnya.

# Library NumPy sering dipakai oleh programmer Python untuk melakukan tugas-tugas dalam ranah science dan engineering karena dianggap memiliki penggunaan penyimpanan memori yang efisien.

matrixs = numpy.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
print(matrixs)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


# mari bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy.
print("Ukuran keseluruhan element list dalam bytes: ", sys.getsizeof(matrix)*len(matrix)) # 240
print("Ukuran keseluruhan element list dalam bytes: ", matrixs.size*matrixs.itemsize) # 36