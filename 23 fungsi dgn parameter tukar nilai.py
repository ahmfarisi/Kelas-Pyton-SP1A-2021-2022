def cetakJudul():
    print('========================')
    print('       Tukar Nilai      ')
    print('========================')

def cetakNilai(m,n):
    print()
    print('a = %d' %m)
    print('b = %d' %n)

def tukarNilai(x,y):
    z = x
    x = y
    y = z
    cetakNilai(x, y)

#panggil
cetakJudul()
a = int(input('a = '))
b = int(input('b = '))
cetakNilai(a, b)
tukarNilai(a, b)