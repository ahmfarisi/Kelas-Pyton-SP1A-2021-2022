import random

angka = random.randint(1, 100)
jawaban = -1
kesempatan = 5

while jawaban != angka :
    jawaban = int(input('Tebak Angka: '))
    
    if jawaban > angka :
        print('Oops! Kebesaran! Tebak Lagi Yok!')
        kesempatan = kesempatan - 1
    elif jawaban < angka :
        print('Oops! Kekecilan! Tebak Lagi Yok!')
        kesempatan = kesempatan - 1
    
    if kesempatan == 0 :
        print()
        print('Maaf, Kesempatan Anda Telah Habis!')
        break
    
    print()

if jawaban == angka :
    print('Selamat Anda Benar')