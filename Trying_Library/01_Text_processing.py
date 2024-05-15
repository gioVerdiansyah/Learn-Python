import re
# String bawaan Python

print("vErDi".upper())
print("VeRdI".lower())
print("verdiiiaaann".count("a"))
print(len("Sofyan Gio Verdiansyah"))

# Regex
if re.match("v...i$", "verdi"):
    print("Is it match")
else:
    print("Is it doesn't match")