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

    jc = 0
    jenisTransaksi = '1'
    
    while jenisTransaksi in ['1', '2']:
        jenisTransaksi = input('Jenis transaksi : ')
        print()

        if jenisTransaksi == '1':
            print('Pembelian')
            print('==================')
            kodeBarang = input('Kode barang   : ')

            if kodeBarang == '1':
                print('Nama barang   : Djarum Coklat')
                jc = int(input('Jumlah barang : '))
                harga = int(input('Harga satuan  : '))
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
                if jc != 0:
                    jc = int(input('Jumlah : '))
                else:
                    print('Stok kosong !')
