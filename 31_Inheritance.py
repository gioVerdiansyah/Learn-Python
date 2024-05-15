# Inheritance (Pewarisan)
# Sebagaimana ilustrasi awal, kita dapat membuat sebuah kelas baru dengan menggunakan kelas induk yang sudah ada. Konsep ini disebut dengan 'inheritance' atau dalam bahasa Indonesia artinya pewarisan.

# Hal yang perlu diperhatikan, jika kelas B memiliki nama metode yang sama dengan kelas A, metode tersebut akan menimpa metode yang diwariskan oleh kelas A.

# Contoh pembuatan pewarisan
# Kelas A
class Car:
    def __init__(self, color, merk, speed):
        self.color = color
        self.merk = merk
        self.speed = speed

    def increase_speed(self):
        self.speed += 10

# Kelas B
class SportCar(Car):
    def turbo(self):
        self.speed += 50

# Contoh penggunaannya
# Kelas A
car_1 = Car("Black", "Avanza", 120)
print(car_1.speed) # 120

# Kelas B
car_2 = SportCar("Blue", "Honda", 120)
print(car_2.speed) # 120
car_2.turbo()
print(car_2.speed) # 170


# Override
# Menimpa method di kelas induk dengan method baru di kelas turunan
# Contoh

class SportCar(Car):
    def turbo(self):
        self.speed += 50

    def increase_speed(self):
        # Method ini lah yg akan di jalankan jika di panggil
        self.speed += 20

sport_car = SportCar("Yellow", "Honda", 120)
print(sport_car.speed) # 120
sport_car.increase_speed()
print(sport_car.speed) # 140



# Super
# Kegunaan menggunakan super class adalah jika kita ingin menggunakan method atau attribute dari kelas induk tanpa menggantinya

class SportCar(Car):
    def turbo(self):
        self.speed += 10

    def increase_speed(self):
        super().increase_speed()
        print("Speed Anda menambah!")

sport_car = SportCar("Black", "Honda", 120)
print(sport_car.speed) # 120
sport_car.increase_speed() # Speed Anda menambah!
print(sport_car.speed) # 130