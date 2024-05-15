# Mendeklarasikan Array
# Pada materi sebelumnya, sudah disebutkan bahwa dalam Python kita dapat mendeklarasikan array menggunakan dua cara. Pertama dengan memanfaatkan list dan kedua menggunakan library Python.

# Perlu Anda ingat, setiap elemen yang ada pada list sebetulnya disimpan pada satu memori. Jika list adalah "[1, 2, 3]", sebetulnya Anda memerintahkan memori komputer untuk menyimpan integer "1" ke dalam satu tempat memori, begitu pun integer "2" akan disimpan dalam satu tempat memori, dan seterusnya.
# Sebagai bukti
my_list = [1,2,3]
for i in my_list:
    print(id(i))

# Alhasil adalah mencetak alamat memory dari satu persatu isi dari array tersebut


# Mendefinisikan Isi Array
# Struktur
# <nama_var> = [<val0>, <val1>, <val2>, ..., <val n-1>]

# Mendefinisikan nilai default
# Struktur
# <nama_val> = [<default_val> for <var> in range(<n>)]

def_arry = [0 for i in range(10)]
print(def_arry) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Meakses array
# Struktur
# <nama_variabel_array>[<index>]

print(my_list[1]) # 2