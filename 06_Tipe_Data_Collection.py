# List []
my_list = [1, "Verdi", True, 3.14]
print(type(my_list)) # <class 'list'>

# List memiliki indeks yang dimulai dari 0
print(my_list[1]) # Verdi

# List dalam python bersifat mutable artinya dapat di ubah
my_list[1] = "Indonesia"
print(my_list) # [1, 'Indonesia', True, 3.14]

# Konsep indexing
props = ["Laptop", "Keyboard", "Mouse", "Mouse Pad"]
print(props[0]) # Laptop
print(props[-1]) # Mouse Pad

# Konsep Splicing
# sequence[start:stop:step]
# start bersifat inklusif(a>=b) sedangkan stop bersifat eksklusif(a>b)
# step default adalah 1, atau tidak melompati element

print(props[0:3:2]) # Laptop Mouse
print(props[1:]) # Keyboard Mouse Mouse Pad
print(props[:2]) # Laptop Keyboard

# Tuple
# Sama dengan list namun nilai yang sudah di deklarasi tidak dapat di ubah

tuple_list = (1, "Verdiansah", False, 1 + 2j)
print(type(tuple_list)) # <class 'tuple'>

# Tuple juga mendukung indexing dan slicing sama seperti list
print(tuple_list[1:])

# Tuple bersifat immunable
# tuple_list[1] = "Indonesia"
# TypeError: 'tuple' object does not support item assignment


# Set
# adalah kumpulan item bersifat unik tanpa ordered collection (tanpa index)
set_list = {1, 2, 3, 4, 4, 1, 2, 3}

# print(set_list[1])
# TypeError: 'set' object is not subscriptable

# Set bersifat unik karena data yang di simpan tidak akan duplikat
print(set_list) # {1, 2, 3, 4}

# Keunikan set yang lain adalah dapat melakukan himpunan matematika, yang dapat Anda gunakan yakni:
# union (gabungan)
# intersection (irisan)

assoc1 = {1,2,3,4,5}
asscoc2 = {4,5,6,7,8}

union = assoc1.union(asscoc2)
print(union) # {1, 2, 3, 4, 5, 6, 7, 8}

intersection = assoc1.intersection(asscoc2)
print(intersection) # {4, 5}


# Dictonary
# kumpulan pasangan key-value yang tidak berurutan
# Definisi dictonary:
# 1. Setiap element berpasangan key dan value di pisahkan dengan koma (,)
# 2. Key dan value di pisahkan dengan titik 2 (:)
# 3. Key dan value bertipe variable/object atau apapun

dictonary = {'name': "Sofyan Gio", 'age': 17, "isMarried": False}
print(type(dictonary)) # <class 'dict'>

# Akan error jika kita mengakses dengan index
# print(dictonary[0]) # KeyError: 0
# Error karena key yang di tuju tidak ada

# Berikut adalah cara mengakses key-value yang benar
print(dictonary['name']) # Sofyan Gio

# Menambahkan data pada dictonary
dictonary['job'] = 'Web Developer'
print(dictonary) # {'name': 'Sofyan Gio', 'age': 17, 'isMarried': False, 'job': 'Web Developer'}

# Menghapus data
del dictonary['isMarried']
print(dictonary) # {'name': 'Sofyan Gio', 'age': 17, 'job': 'Web Developer'}

# Mengubah data pada dictonary
dictonary['name'] = "Verdiansyah"
print(dictonary)