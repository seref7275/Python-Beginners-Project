import time
import datetime

print("Bu uygulama yazı hızınızı ölçer.")

print("Uygulama başlıyor.")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go")

baslangic = datetime.datetime.now()

yazi = input("Yazı giriniz: ")

bitis = datetime.datetime.now()

yazıhizi = bitis - baslangic

karakter = int(len(yazi))
bosluk = yazi.strip()
speed = round(yazıhizi.total_seconds(),2)

hiz = karakter / speed


print(f"{yazi} : yazısını {speed} saniye içerisinde {karakter} karakter olarak yazdınız. TEBRİKLER.")
print(f" 1 saniye içerisinde {hiz} karakter yazabilirsiniz . TEBRİKLER.")




























