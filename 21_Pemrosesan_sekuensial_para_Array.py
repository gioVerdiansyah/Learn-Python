# Pemrosesan Sekuensial pada Array
# Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array.
#
# Adapun pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.
#
# Sebab pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang perlu diperhatikan.
#
# 1. Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
# 2. Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0.
# 3. Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
# 4. Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
# 5. Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.

# Contoh
my_arry = [1,2,3,4,5]
for i in range(len(my_arry)):
    current_element = my_arry[i]
    next_index = i+1

    if next_index < len(my_arry):
        next_element = my_arry[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, Next element: {next_element}")