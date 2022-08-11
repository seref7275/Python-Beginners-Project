
print('Bu hesap makinasında 1,2,3,4 kullanılarak işlem yapılmaktadır (1-Toplama 2-Çıkarma 3-Çarpma 4-Bölme)')

islem = float(input('Yapmak istediğini işlemi girin:'))

sayi1 = float(input('Sayı giriniz: '))
sayi2 = float(input('Sayı giriniz: '))

if islem == 1:
    print(sayi1+sayi2)
elif islem == 2:
    print(sayi1-sayi2)
elif islem == 3:
    print(sayi1*sayi2)
elif islem == 4:
    print(sayi1/sayi2)
else: 
    print('Geçersiz tuşlama...')
















