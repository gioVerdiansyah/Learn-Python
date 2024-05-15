# Definisi Subprogram
# Semakin besar sebuah program, bagian kode yang berulang akan bertambah sehingga tidak efisien jika Anda perlu mengetik ulang atau bahkan melakukan copy-paste. Salah satu kode yang sering berulang adalah rumus atau formula.
# Contoh

w1 = 50
h1 = 30

result1 = w1 * h1
print(result1) # 1500

w2 = 40
h2 = 80

result2 = w2 * h2
print(result2) # 3200

# Solusinya adalah membuat sebuah fungsi
# Fungsi di Python

def searches_square(width, height):
    return width * height

# Contoh penggunaannya
print(searches_square(30, 50)) # 1500