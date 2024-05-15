import os
import json
import pickle

# OS
print(os.getcwd()) # Currrent work directory

# JSON
with open("resources/data_persoal_example.json") as file:
    print(json.load(file)['name'])

json_data = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
print(json.loads(json_data)['nama'])


# Pickle
# Jika Anda memiliki sebuah list yang ingin disimpan atau ditransmisikan tanpa khawatir bentuknya akan rusak atau kacau, fungsi dari library pickle dapat dimanfaatkan.

# contoh cara melakukan proses pickle pada sebuah object dictionary dan menyimpannya pada sebuah file.
dict_data = {1:"5", 2:"4", 3:"3", 4:"2", 5:"1"}
pickle_out = open("resources/dict.pickle", "wb")
pickle.dump(dict_data, pickle_out)
pickle_out.close()


# contoh untuk mengekstraksi berkas pickle dan menaruhnya pada sebuah variabel.
pickle_enter = open("resources/dict.pickle", "rb")
dist_example = pickle.load(pickle_enter)
pickle_enter.close()

print(dist_example)