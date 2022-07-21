#cara 1
angka = [1,2,3,4]
pangkat = []

for i in angka :
    pangkat.append(i**2)

print(pangkat)

#cara 2
angka = [1,2,3,4]
pangkat = [i**2 for i in angka]
print(pangkat)