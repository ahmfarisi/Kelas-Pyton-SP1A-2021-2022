import sys

print('Toko Sembako Palembang')
print('----------------------')
print('Daftar harga sembako:')
print('1. Telur   Rp 25.000/kg')
print('2. Minyak  Rp 14.000/liter')
print('3. Beras   Rp 85.000/10 kg')

pilih  = int(input('Pilih Produk: '))

if pilih == 1 :
    produk = 'Telur (/Kg)'
    harga  = 25000
elif pilih == 2 :
    produk = 'Minyak (/Ltr)'
    harga = 14000
elif pilih == 3 :
    produk = 'Beras (/10 Kg)'
    harga = 85000
else :
    print('Maaf, Produk Tidak Tersedia')
    sys.exit()
    
jumlah = int(input('Jumlah      : '))

hargaJual = jumlah * harga

if hargaJual > 200000 :
    potongan = 25000
elif hargaJual >= 100000 and hargaJual <=199999 :
    potongan = 15000
elif hargaJual >= 50000 and hargaJual <= 99999 :
    potongan = 7500
else :
    potongan = 0

total = hargaJual - potongan

print()
print('--------------------------')
print('       NOTA PEMBELIAN     ')
print('--------------------------')
print('Barang       : %s' %produk)
print('Harga Barang : Rp %d' %harga)
print('Jumlah       : %d' %jumlah)
print('Subtotal     : Rp %d' %hargaJual)
print('Potongan     : Rp %d' %potongan)
print('--------------------------')
print('Total        : Rp %d' %total)
