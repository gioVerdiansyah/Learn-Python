# Nama          Deskripsi                                               Contoh
# Class         Cetakan (blueprint) untuk membuat objek-objek           Mobil; Manusia.
#               yang memiliki karakteristik dan perilaku serupa.
# Object        Perwujudan dari class                                   Mobil Dicoding; Budi
# Method        Perilaku atau tindakan yang dapat dilakukan oleh        Maju, Mundur, Berhenti
#               objek atau kelas.
# Attribute     Variabel yang menjadi identitas dari objek atau kelas.  Warna, kecepatan, merek.


# Class
# Contoh pembuatan class

class Car:
    # Attribute
    color = "Blue"

# Object
# Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Berdasarkan KBBI dari kemendikbud, objek merupakan benda, hal, dan sebagainya yang dijadikan sasaran untuk diteliti, diperhatikan, dan sebagainya. Keterkaitan antara objek dan class sangat erat. Contohnya, jika Anda membuat kelas bernama manusia, objeknya adalah manusia dengan nama yang berbeda.

# Untuk memanggilnya, kita harus mengubahnya menjadi bentuk yang lebih nyata atau bisa dikatakan objek dari kelas tersebut perlu dibuat.

my_car = Car()
print(my_car.color) # Blue


# Attribute
# Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama.

# Namun, perlu diperhatikan bahwa jenis atribut kelas memiliki kelemahan, yaitu ketika nilai atribut kelas diubah, perubahan tersebut akan memengaruhi semua objek yang dibuat berdasarkan kelas tersebut.

Car.color = "Red"
print(Car.color) # Red


# Class Constructor
# Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas.

class Car:
    def __init__(self):
        self.color = "Purple"

my_car = Car()

print(my_car.color) # Purple

# Penggunaan class sesuai kebutuhan
class Car:
    def __init__(self, color, merk, speed):
        self.color = color
        self.merk = merk
        self.speed = speed

# Penggunaaan
my_car = Car("Black","Avanza", "120/h")
print(my_car.speed)




# Method
# Setelah atribut, saatnya membahas method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode. Python membagi method menjadi tiga jenis.

# Metode dari object (object method).
# Metode secara statis (static method).
# Metode dari class (class method).
# Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja.

# Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal.  Contoh sederhana dekorator sebagai berikut.

def my_dec(func):
    def wrap():
        print("Begin")
        func()
        print("End")
    return wrap

# Dekorasi fungsi dengan decorator
@my_dec
def say():
    print("Hello World")

say()
# Begin
# Hello World
# End


# Metode dari Objek (Object Method)
#  Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini.

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def increase_speed(self):
        self.speed += 10

# Contoh penggunaannya
my_car = Car("Black", 150)
print(my_car.speed) # 150
my_car.increase_speed()
print(my_car.speed) # 160


# Metode secara Statis (Static Method)
# Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.

class Car:
    def __init__(self, merk):
        self.merk = merk

    @staticmethod
    def intro():
        print("Ini adalah static method")

Car.intro()
my_car = Car("Avanza")
my_car.intro() # juga bisa


# Metode dari Kelas (Class Method)
# Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas. Mari buat contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan class method.

class Car:
    def __init__(self, merk):
        self.merk = merk

    @classmethod
    def intro(cls):
        print("Ini adalah class method")


Car.intro()
my_car = Car("Daihatsu")
my_car.intro() # Juga bisa