# Jenis-Jenis Ekspresi
# Pada dasarnya, jenis-jenis ekspresi dibagi menjadi dua. Pertama adalah menurut jumlah operan (arity) dari operator dan kedua adalah menurut tipe data yang dihasilkan.

# Ekspresi Menurut Arity dari Operator
# Jenis     Contoh
# Biner     (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y)
# Uner      (x += 1), (x-=1), (not x)


# Ekspresi biner merupakan jenis yang memiliki dua operan
# Ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan

# Contoh ekspresi uner
a = True
a = not a
print(a) # False
# Operator not membalikan nilai boolean, misal True menjadi False begitupun sebaliknya

b = 6
b -= 1
print(b) # 5
# Decrement, seolah-olah seperti mengurangi dirinya sendiri, namun aslinya seperti ini
# b = b - 1

c = 10
c -= 2
print(c) # 8
# Increment, konsepnya seperti decrement namun di tambah

d = 20
print(-d) # -20
# menjadi bilangan negative


# Ekspresi Menurut Tipe Data yang Dihasilkan

# Jenis                                             Contoh
# Ekspresi aritmetika:                              2 + 2 = 4, 2 - 2 = 0
# <numerik> <operator> <numerik> = <numerik>
# Ekspresi relasional:                              3 < 10 = True, 1 > 10 = False
# <numerik> <operator> <numerik> = <boolean>
# Ekspresi logika:                                  True or False = True
# <boolean> <operator> <boolean> = <boolean>

# Contoh
print(2+2) # 4
print(8-3) # 5
print(True or False) # True