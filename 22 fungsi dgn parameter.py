def cetakJudul():
    print('================================')
    print('Program Menghitung Luas Segitiga')
    print('================================')

def hitungLuasSegitiga(alas, tinggi):
    luas   = alas * tinggi / 2
    print('Luas Segitiga adalah %.2f' %luas)

#panggil
cetakJudul()
a = int(input('Alas   = '))
t = int(input('Tinggi = '))
hitungLuasSegitiga(a, t)