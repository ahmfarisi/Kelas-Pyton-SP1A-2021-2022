def cetakJudul():
    print('================================')
    print('Program Menghitung Luas Segitiga')
    print('================================')

def hitungLuasSegitiga():
    global luas
    alas   = int(input('Alas   = '))
    tinggi = int(input('Tinggi = '))
    luas   = alas * tinggi / 2

def cetakHasil():
    global luas
    print('Luas Segitiga adalah %.2f' %luas)

#panggil
cetakJudul()
hitungLuasSegitiga()
cetakHasil()