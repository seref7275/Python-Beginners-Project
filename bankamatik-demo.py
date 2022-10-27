# Bankamatik uygulaması
# abs mutlak değer içerisine alır 
hesap1 = {
    'hesapnumarası':'123456',
    'isim':' Şeref',
    'dogumyılı':'2002',
    'hesapbakiyesi':200,
    'nakitavans':- 150,
    'ekhesap': 10000
}



hesap2 = {
    'hesapnumarası':'654321',
    'isim':'Ahmet',
    'dogumyılı':'2001',
    'hesapbakiyesi':1800,
    'nakitavans':400,
    'ekhesap': 3000
}


hesap3 = {
    'hesapnumarası':'987654',
    'isim':'Ayşe',
    'dogumyılı':'2003',
    'hesapbakiyesi':700,
    'nakitavans':200,
    'ekhesap': 2700
}


def para_yatirma(hesap,miktar):
    print(f"Para yatırma işleminiz başarıyla gerçekleşmiştir yeni bakiyeniz: {hesap['hesapbakiyesi'] + miktar}")

def para_cekme(hesap,miktar):
    if (miktar > hesap['hesapbakiyesi']):
        print(f"Hesap bakiyeniz:{hesap['hesapbakiyesi']}, Çekmek istediğiniz tutar:{miktar} bakiyeniz yetersizdir lütfen geçerli bir miktar giriniz.")
        nakitavans = input('Nakit avans almak istermisiniz ? : (e/h) : ')
        if miktar > hesap['hesapbakiyesi'] and nakitavans=='h':
            print('nakit avans işleminiz iptal edilmiştir')
            if hesap['ekhesap'] > miktar:
                ekhesap = input(f"'Ek hesaptan para çekmek istermisiniz ? Ek Hesap bakiyeniz: {hesap['ekhesap']}: (e/h) : ")
                if hesap['ekhesap'] > miktar and ekhesap == 'h':
                    print('Ek hesap para çekme işleminiz reddedilmiştir.')
                elif hesap['ekhesap'] > miktar and ekhesap == 'e':
                    print(f"Ek hesaptan para çekme işleminiz gerçekleşmiştir kalan ek hesap bakiyeniz: {hesap['ekhesap'] - miktar}")
                else:
                    print('ek hesap bakiyeniz yetersizdir.')            
        elif miktar > hesap['hesapbakiyesi'] and nakitavans == 'e':
            print(f"{hesap['nakitavans']}: TL nakit avans çekilmiştir. Nakit avans bakiyeniz: {-1*hesap['nakitavans']}")
    else:
        print(f"Para çekme işleminiz onaylanmıştır geriye kalan hesap bakiyesi: {hesap['hesapbakiyesi'] - miktar}")

 
def bakiye_sorgulama(hesap):
    print('Hesap bakiye sorgulama üceri 2 TL.')
    if hesap['hesapbakiyesi'] < 2:
        print("Hesap bakiyeniz sorgulanamadı.")
    else:
        print(f"Hesap bakiyeniz: {hesap['hesapbakiyesi'] - 2}")
    

def nakit_avans_yatırma(hesap,miktar):
    if hesap['nakitavans'] < 0 :
        print(f"Nakit avans bakiyeniz: {hesap['nakitavans']}")
        miktar = int(input('Yatırmak istediğiniz tutarı giriniz: '))
        print(f"Yeni nakit avans bakiyeniz {miktar + hesap['nakitavans']}")
    else:
        print('Nakit avans borcunuz bulunmamaktadır.')



islem = para_cekme(hesap1,1000)
print(islem)



# islem = nakit_avans_yatırma(hesap1,150)
# print(islem)




# islem = para_yatirma(hesap2,500)
# print(islem)


# islem = para_cekme(hesap2,5000)
# print(islem)



# islem = bakiye_sorgulama(hesap2)
# print(islem)


















