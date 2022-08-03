def cetakJudul():
    print('================================')
    print('Program Menghitung Luas Segitiga')
    print('================================')

def hitungLuasSegitiga():
    alas   = int(input('Alas   = '))
    tinggi = int(input('Tinggi = '))
    luas   = alas * tinggi / 2
    print('Luas Segitiga adalah %.2f' %luas)

#panggil
cetakJudul()
hitungLuasSegitiga()