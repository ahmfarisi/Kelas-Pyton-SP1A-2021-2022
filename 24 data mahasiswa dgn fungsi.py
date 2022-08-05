def cetakJudul():
    print('=======================')
    print('Aplikasi Data Mahasiswa')
    print('=======================')

def inputDataMahasiswa(jumlah):
    global namaMhs
    namaMhs = []
    for i in range(jumlah):
        namaMhs.append(input('Nama Mahasiswa   : '))

def tampilDataMahasiswa():
    global namaMhs
    
    print()
    print('--------------------')
    print('No\tNama')
    print('--------------------')
    for i in range(len(namaMhs)):
        print('%d\t%s' %(i+1, namaMhs[i]))

#panggil
cetakJudul()
n = int(input('Jumlah Mahasiswa : '))
inputDataMahasiswa(n)
tampilDataMahasiswa()