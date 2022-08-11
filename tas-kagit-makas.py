import random
from tracemalloc import stop


secenek = ["taş","kağıt","makas"]

tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]
print("Taş Kağıt Makas Uygulamasına  Hoşgeldiniz")
print("1 İle 10 arası hakkınız olacaktır her kaybettiginizde 1 hakkınız yanacaktır.")
print("Uygulamadan çıkmak istiyorsanız q tuşuna basabilirsiniz.")
hak = int(input("Kaç hak istersiniz (1-10 arası hak isteyiniz) : "))
# if 0< hak < 10:
#     print('sw')
# else:
#     print("Fazla Hak girdiniz.")
#     stop


while hak > 0:
    secim = input("Taş Kağıt Makas Seçiminizi yapınız: ")
    bil_secim = random.choice(secenek)
    bil_secim.lower()
    if secim == tas:
        if bil_secim == tas:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Berabere")
        elif bil_secim == kagit:
            hak -= 1 
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kaybettiniz Kalan hakkınız {hak}")
        else:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kazandınız")
    if secim == kagit:
        if bil_secim == kagit:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Berabere")
        elif bil_secim == tas:
            hak -= 1
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kaybettiniz Kalan hakkınız {hak}")
        else:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kazandınız")
    if secim == makas:
        if bil_secim == makas:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Berabere")
        elif bil_secim == kagit:
            hak -= 1
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kaybettiniz Kalan hakkınız {hak}")
        else:
            print(f"Seçiminiz: {secim} Bilgisayarın Seçimi: {bil_secim} Durum: Kazandınız")
    
    if secim == "q" :
        print("Uygulamadan Çıkılıyor")
        break
    



















