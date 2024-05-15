import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas
data = {
    "name": ["Verdi", "Adi", "Niam", "Beta"],
    "age": [16,17,16,16],
    "profession": ["BackEnd", "FrontEnd", "Designer", "Designer"]
}

df = pd.DataFrame(data)

print(df)

# NumPy
matrix = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)


# Matplotlib

# Data
x = [1,2,3,4,5,6]
y = [9,8,7,6,5,4]

# Membuat plot dari data
plt.plot(x,y)

# Menambah deskripsi plot
plt.title("My Data")
plt.xlabel("Width")
plt.ylabel("Height")

# menampilkan
plt.show()



# Seaborn

# Contoh data
tips = sns.load_dataset("tips")

# Contoh plot histrogram
sns.histplot(tips['total_bill'], kde=True)
plt.title("Dummy Data")
plt.xlabel("Propperties")
plt.ylabel("Much data")

plt.show()