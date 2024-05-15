# Integer ke Float
print(float(5)) # 5.0

# Float ke Integer
print(int(5.6)) # 5
print(int(-5.6)) # -5

# Konversi data-dan-ke string
print(int("25")) # 25
print(float("25")) # 25.0
print(str(25)) # 25
print(str(25.0)) # 25.0

# Jika nilai tidak valid
# print(int("1p"))
# ValueError: invalid literal for int() with base 10: '1p'

# Konversi kumpulan data
print(set([1,2,3])) # {1, 2, 3}
print(tuple({4,5,6})) # (4, 5, 6)
print(list("Hello")) # ['H', 'e', 'l', 'l', 'o']

# Konversi ke dictonary
print(dict([[1,2], [3,4]])) # {1: 2, 3: 4}
# Bisa juga menggunakan tuple atau set
