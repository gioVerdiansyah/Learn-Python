# Latihan Array
# Pemrosesan array merujuk pada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Salah satu operasinya adalah pemrosesan sekuensial yang merupakan sebuah pemrosesan setiap elemen array, dimulai dari elemen pada indeks terkecil hingga indeks terbesar.
#
# Dari sekian banyaknya contoh pemrosesan sekuensial pada array, mari kita pelajari salah satunya, yakni mencari nilai terbesar dalam array.

# Kita memiliki array yang beranggotakan nilai integer dengan elemen indeks ke-0 adalah 1, elemen indeks ke-1 adalah 7, elemen indeks ke-2 adalah 2, elemen indeks ke-3 adalah 89, elemen indeks ke-4 adalah 3.
#
# Kita akan mencari nilai atau elemen terbesar dari array tersebut menggunakan algoritma two pointers. Algoritma adalah serangkaian langkah-langkah terstruktur yang dirancang untuk menyelesaikan suatu masalah atau mencapai suatu tujuan. Dalam hal ini, tujuan yang ingin dicapai adalah mencari nilai terbesar pada array.
#
# Algoritma two pointers adalah algoritma yang memiliki pendekatan dengan cara memanipulasi atau memproses urutan data menggunakan dua penanda atau dua pointer secara bersamaan. Kedua pointer tersebut bisa kita sebut sebagai "left" dan "right".


# Untuk memahami algoritma ini, perhatikan beberapa informasi berikut.
#
# 1. Pointer "left" akan berada pada indeks pertama dan menyatakan bahwa pointer "left" selalu menunjukkan nilai terbesar dalam array.
# 2. Pointer "right" akan selalu berada pada elemen selanjutnya dan membandingkannya dengan elemen pointer "left".

# Pertama, kita memulai dengan dua pointer: pointer "left" pada elemen pertama (1) dan pointer "right" pada elemen berikutnya (7). Kita membandingkan nilai 7 dengan nilai 1. Sebab 7 lebih besar dari 1, kita mengganti nilai pointer "left" dari 1 menjadi 7.
# Sekarang, pointer "left" berada pada elemen 7 dan pointer "right" berada pada elemen berikutnya (2). Kita membandingkan nilai 7 dengan 2. Sebab 2 tidak lebih besar dari 7, pointer "left" tetap pada nilai 7.
# Pointer "right" berpindah ke elemen berikutnya (89), sementara pointer "left" tetap pada nilai 7. Kita membandingkan nilai 89 dengan 7. Sebab 89 lebih besar dari 7, pointer "left" berpindah ke nilai 89.
# Sekarang, pointer "left" berada pada elemen 89 dan pointer "right" berada pada elemen berikutnya (3). Kita membandingkan nilai 89 dengan 3. Sebab 3 tidak lebih besar dari 89, pointer "left" tetap pada nilai 89.
# Proses berakhir, nilai pada pointer "left" ditetapkan sebagai nilai terbesar dalam array.

my_arry = [1,7,2,89,3]

# my
true_val = my_arry[0]
for i in range(len(my_arry)):
    right = my_arry[len(my_arry) - 1 if i + 1 < len(my_arry) else i]
    left = my_arry[i]
    if left > right:
        true_val = left

print(true_val)

# dicoding
left = my_arry[0]
for i in range(1, len(my_arry)):
    right = my_arry[i]
    if right > left:
        left = right
print(left)