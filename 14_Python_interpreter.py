# Python Interpreter
# Kode dari program Python yang Anda bangun akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan program compiler atau interpreter. Compiler merupakan program yang akan menerjemahkan bahasa pemrograman menjadi bahasa mesin sebelum dijalankan dan menghasilkan output. Ini artinya program yang Anda bangun secara keseluruhan akan diubah terlebih dahulu semuanya menjadi bahasa mesin.
# Compiler works
# Source Code -> Compiler -> Machine Code -> Output
# Interpreter works
# Source Code -> Interpreter -> Output

# Hal berbeda terjadi pada interpreter, yang akan menerjemahkan bahasa Python satu per satu dan menghasilkan output secara langsung. Hal ini memungkinkan Anda untuk melihat hasil program segera setelah satu baris kode dieksekusi hingga selesai. Implementasi interpreter ada pada mode interaktif Python. Anda dapat menjalankan satu atau dua lebih baris kode secara langsung dan melihat hasilnya.
#
# Python memiliki aturan yang membantu Anda untuk menulis kode dengan baik dan benar. Guido van Rossum selaku pembuat bahasa Python merasa bahwa kode lebih sering dibaca dibandingkan ditulis. Dengan membuat kode yang baik dan benar akan memudahkan Anda untuk memahami kode bahkan membantu interpreter atau compiler berjalan dengan baik.


# Block Code
# Sebuah program Python dapat berupa pernyataan atau statement, bisa juga terdiri atas blok kode. Sebuah blok merujuk pada potongan kode program Python yang dijalankan sebagai satu unit. Kode blok dapat berupa modul, fungsi, kelas, control flow, dan sebagainya.

for i in range(10):
    print(i + 1)

# Perhatikan bahwa kode perulangan di atas juga melakukan aksi sekuensial, yakni setiap kode akan dijalankan lalu diulangi hingga kondisi akhir terpenuhi.
# Mengapa memahami kode blok penting? Alasannya adalah Anda harus membuat kode yang mudah dimengerti oleh Anda dan orang lain sebagai seorang programmer. Selain itu, kode blok yang baik dan benar akan memudahkan interpreter atau compiler untuk berjalan dengan baik dan tidak menghasilkan error.
# Contoh khasus:
# for i in range(10):
# print(i + 1)
# Akan error: IndentationError: expected an indented block
# Program akan menghasilkan error karena interpreter akan menganggap bahwa kode "print(i)" merupakan bagian dari kode blok "for i in range(10)". Error dihasilkan karena harusnya terdapat indentasi (biasanya berupa empat spasi) sebelum kode "print(i)".

# Python sangat memperhatikan indentasi karena hal tersebut tidak hanya membantu merapikan kode yang Anda bangun, tetapi juga menjelaskan satu kode blok secara utuh. Dengan indentasi, program akan mengetahui letak awal dan akhir sebuah blok kode. Ke depannya, Anda akan melihat sebuah fungsi, modul, dan kelas yang ada dalam Python juga dengan memperhatikan indentasi untuk menyatakan kode blok secara utuh.



# Case-sensitive
# Python termasuk bahasa pemrograman case-sensitive. Ini artinya Python memperlakukan huruf besar dan kecil sebagai karakter yang berbeda dalam penamaan variabel, nama fungsi, atau penulisan kode secara umum.
teks = "Verdiansyah"
Teks = "Indonesia"

print(teks)
print(Teks)
# print(TEks) # Akan error variabel tidak ditemukan