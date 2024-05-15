# Tipe data primitif

# Integer
val = 47
print(type(val))

# Float
val = 3.14
print(type(val))

# Complex
val = 1 + 2j
print(type(val))

# <class 'int'>
# <class 'float'>
# <class 'complex'>


# Tipe data number adalah immutable yang artinya nilai di dalam nya tidak dapat berubah
var = 10
print(var)
print(id(var))

var = 20
print(var)
print(id(var))

# 10
# 140705081234504
# 20
# 140705081234824

# Angka setelah 10 dan 20 tersebut adalah memory address
# Jadi alih-alih kita mengganti nilai dalam variabel nyatanya kita malah membuat objek baru pada variabel tersebut

# Boolean
boolVal = True
print(boolVal)
print(type(boolVal))

boolVal = False
print(boolVal)
print(type(boolVal))

# True
# <class 'bool'>
# False
# <class 'bool'>

# String
strVal = 'Verdi'
print(type(strVal)) # <class 'str'>

# multi line
multiLine = """
Hello
nama saya adalah
verdi
"""

print(multiLine)

# String juga merupakan urutan karakter yang setiap karakternya memiliki indeks

print(strVal[0]) # V
# Meskipun memiliki indeks namun Anda tidak dapat mengubah isi di dalam indeks tersebut

# strVal[0] = 'F'
# TypeError: 'str' object does not support item assignment

# Metode indexing dan slicing
print(strVal[1:]) # erdi
print(strVal[1:3]) # er

# String formatted
name = "Sofyan Gio"
lastName = "Verdiansyah"
print(f"Hallo nama saya adalah {name} {lastName}")
print("Hallo nama saya adalah %s %s" % (name, lastName))
print("Hallo nama saya adalah {} {}" .format(name, lastName))