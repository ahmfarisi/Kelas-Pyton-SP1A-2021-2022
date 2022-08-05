def cetakJudul():
    print('=======================')
    print('Aplikasi Data Mahasiswa')
    print('=======================')

def inputDataMahasiswa(jumlah):
    global namaMhs, npmMhs, prodiMhs
    namaMhs = []
    npmMhs = []
    prodiMhs = []
    
    for i in range(jumlah):
        print()
        namaMhs.append(input('Nama Mahasiswa   : '))
        npmMhs.append(input('NPM Mahasiswa    : '))
        prodiMhs.append(input('Prodi Mahasiswa  :'))

def tampilDataMahasiswa():
    global namaMhs
    
    print()
    print('------------------------------------')
    print('No\tNama\t\tNPM\tProgram Studi')
    print('------------------------------------')
    for i in range(len(namaMhs)):
        print('%d\t%s\t%s\t%s' %(i+1, namaMhs[i], npmMhs[i], prodiMhs[i]))

#panggil
cetakJudul()
n = int(input('Jumlah Mahasiswa : '))
inputDataMahasiswa(n)
tampilDataMahasiswa()