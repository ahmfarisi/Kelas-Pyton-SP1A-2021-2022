print('Input Data Mahasiswa')
print('--------------------')
n = int(input('Jumlah : '))

mhs = []

print()
for i in range(n):
    # mhs.append(input('Nama Mahasiswa Ke {}: '.format(i+1)))
    mhs.append(input('Nama Mahasiswa Ke %d : ' %(i+1)))

print()
print('Data Mahasiswa Terdaftar')
for i in range(n):
    print('%d. %s' %((i+1), mhs[i]))