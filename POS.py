import locale

#https://stackoverflow.com/questions/320929/currency-formatting-in-python
print(locale.setlocale( locale.LC_ALL, '' ))
print()

password = input('Password : ')

if password == 'kyakyakya':
    print('Sukses login !')
    print()

    print('1. Pembelian')
    print('2. Penjualan')

    jenisTransaksi = input('Jenis transaksi : ')
    print()

    if jenisTransaksi == '1':
        print('Pembelian')
        print('==================')
        kodeBarang = input('Kode barang : ')

        if kodeBarang == '1':
            print('Djarum Coklat')
            jc = int(input('Jumlah : '))
            harga = int(input('Harga satuan : '))
            print('Total harga pembelian :',  locale.currency(jc * harga, grouping = True ))

            print()
            print('Stok DJarum Coklat')
            print('==================')
            print('Jumlah barang : ', jc)
            print('Nilai stok    : ', jc * harga)

    if jenisTransaksi == '2':
        print('Penjualan')
        print('==================')
        kodeBarang = input('Kode barang : ')

        if kodeBarang == '1':
            print('Djarum Coklat')
            jc = int(input('Jumlah : '))
