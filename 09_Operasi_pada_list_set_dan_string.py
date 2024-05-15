# len()
# Bertujuan untuk menghitung panjang pada suatu list, set atau string
my_list = [1,2,3,4,'hello']
my_set = {1,2,3,4,5,6,7,8,9,10}
print(len(my_list)) # 5
print(len(my_set)) # 10
print(len("Belajar Data Scientist")) # 22 Termasuk spasi


# min() dan max()
# Digunakan mencari nilai terendah dan tertinggi
number = [3,1,5,1,6,7,4,6,8,9,4,6,3]
print(max(number)) # 9
print(min(number)) # 1
print(min("Hallo")) # H
print(max("Hallo")) # o

# count
# Digunakan untuk mencari objek yang di maksud muncul berapa kali
print(number.count(3)) # 2
print("Hello".count('l')) # 2


# in dan not in
# Digunakan untuk mengetahui object yang dimaksud ada atau tidak dalam list. Operator ini mengembalikan nilai boolean

sentence = "Belajar Python untuk menjadi Data Scientist"
print("Python" in sentence) # True
print("Machine Learning" in sentence) # False
print("JavaScript" not in sentence) # True
print(4 in number) # True



# Multiple variabel
# Contoh khasus:
data = ["Laptop Asus", "AMD Ryzen", "8GB"]
# unit = data[0]
# processor = data[1]
# ram = data[2]

# Dari pada menggunakan cara di atas ada cara yang lebih efesien:
unit, processor, ram = data
print(unit)
print(processor)
print(ram)


# sort()
# Digunakan untuk mengurutkan angka ataupun huruf
transports = ["train", "bus", "plane", "car"]
transports.sort()
print(transports)

# reverse
transports.sort(reverse=True)
print(transports)

# Tidak bisa angka dan string dalam list
# Jika ada maka akan error
# sorter = ['hello', 1, 'python', 2]
# sorter.sort()
# print(sorter)
# TypeError: '<' not supported between instances of 'int' and 'str'


# sort menggunakan metode ASCII
# Jadi jika ada kata atau kalimat kapital akan di dahulukan
ascii_example = ["laptop", 'keyboard', 'Mouse', 'charger']
ascii_example.sort()
print(ascii_example) # ['Mouse', 'charger', 'keyboard', 'laptop']


# Jika ada angka berupa string
# Maka akan di dahulukan daripada huruf kapital
sorter = ["laptop", "keyboard", "Mouse", "100", "charger"]
sorter.sort()
print(sorter) # ['100', 'Mouse', 'charger', 'keyboard', 'laptop']