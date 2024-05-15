# Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.
#
# Struktur umum ekspresi yang sering dijumpai adalah <operan1> <operator> <operan2>. Namun, perlu Anda ketahui bahwa struktur umum tersebut merupakan struktur ekspresi biner (jenis ekspresi menggunakan dua operan). Mari bedah struktur tersebut lebih dalam.

# 1. Operan dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
# 2. Operator merupakan suatu fungsi standar yang disediakan dalam bahasa pemrograman untuk melakukan beberapa hal dasar, seperti perhitungan aritmetika, logika, dan relasional. Contohnya adalah penjumlahan (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.

# contoh
x = 10
y = 2
result = x - y
print(result) # 8


# Penggabungan dan replika pada list
# Penggabungan
numbers = [3,4,5,6]
words = ['P', 'Y', 'T', 'H', 'O', 'N']
join = numbers + words
print(join) # [3, 4, 5, 6, 'P', 'Y', 'T', 'H', 'O', 'N']

# replika
replica = words * 2
print(replica) # ['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']