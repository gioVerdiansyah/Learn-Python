# Uppercase and Lowercase
print("Verdi".upper()) # VERDI
print("Verdi".lower()) # verdi

# Beginning and Ending (Menghapus whitespace)
print("Verdi        ".rstrip()) # Menghapus whitespace dari kanan
print("         Verdi".lstrip()) # Menghapus whitespace dari kiri
print("     Verdi       ".strip()) # Menghapus whitespace dari kanan kiri
print("lalalalaVerdilalalala".strip("la")) # dapat juga menghapus suatu kata dalam string

print("Sofyan Gio".startswith("Sofyan")) # mengecek apakah awal string di awali dengan apa yang di maksud
print("Sofyan Gio".endswith("Sofyan")) # mengecek apakah akhir string di akhiri dengan apa yang di maksud

# Memisahkan dan menggabungkan string
# Menggabungkan
print(" ".join(["Sofyan", "Gio", "Verdi"])) # Delimiter di sini adalah whitespace, contoh menggunakan delimiter lain
print("-".join(["Dicoding", "Indonesia"]))

# Memisahkan
print("Sofyan Gio".split())
print("""Hallo
nama saya
adalah sofyan""".split("\n")) # ['Hallo', 'nama saya', 'adalah sofyan']


# Pengecekan String
print("VERDI".isupper()) # Mengecek apakah semua huruf besar
print("verdi".lower()) # Mengecek apakah semua huruf kecil
print("sofyan".isalpha()) # Mengecek apakah semua huruf adalah alphabet
print("sofyan123".isalnum()) # Mengecek apakah semua huruf adalah alphanumerik
print("123".isdecimal()) # Mengecek apakah semua huruf adalah berupa bilangan angka
print('     '
      ''.isspace()) # Mengecek apakah string berisi whitespace atau newline
print("Filosofi Teras".istitle()) # Mengecek apakah setiap kata kapital


# Formatting pada string
print("code".zfill(5)) # berfungsi melengkapi panjang string dari parameter dengan 0
print('verdi'.rjust(20)) # untuk membuat teks menjadi rata kanan
print('verdi'.rjust(20, '_')) # whitespace dapat diganti dengan karakter
print('verdi'.ljust(20)) # sama, namun membuat rata teks menjadi rata kiri
print('verdiansyah'.center(25, '-')) # membuat teks menjadi rata tengah, whitespace dapat di ganti dengan karakter


# String literals
# \' single quote
# \" double quote
# \t tab
# \n new line
# \\ backslash

print("Hallo\nKapan terakhir kita bertemu?\nHari jum\'at lalu.")
# Hallo
# Kapan terakhir kita bertemu?
# Hari jum'at lalu.

# Raw String
# Print semua yang saya masukan tidak peduli itu string literals ataupun apapun
print(r"Hello\nVerdi")