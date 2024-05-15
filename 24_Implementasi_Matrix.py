# Implementasi Matriks pada Python

# Deklarasi Matriks
# Deklarasi sekaligus inisialisasi nilai matriks.
# Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM). Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.
# <nama_val> = [[<val_12>, <val_13>, ..., <val_1m>]
#               [<val_22>, <val_23>, ..., <val_2m>]
#                   ...
#                [<val_n1>, <val_n2>, ..., <val_nm>]]

# Contoh
matrix = [[1,0,1,0,1],
           [0,1,0,1,0],
           [1,0,1,0,1]]
print(matrix) # [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]

# Deklarasi dengan nilai default
# Cara kedua adalah mendeklarasikan matriks dengan nilai default. Sebagaimana materi array, nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan dengan nilainya di luar rentang yang ditentukan. Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. Kita bisa menyepakati nilai "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10). Cara kedua ini melibatkan list comprehension yang sama seperti pada materi array.
# Struktur
# <nama_var> = [[<default_val> for j in range(<m>)] for i in range(<n>)]

default_matrix = [[0 for j in range(4)] for i in range(3)]
print(default_matrix) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Akses Elemen Matriks
# Struktur
# <nama_var_matrix>[nbrs][nkol]

rand_matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
print(rand_matrix[1][2]) # 6