import time
import random

bosluk = 10 * " "
giris = " Zar atma Uygulamasına Hoşgeldiniz "
metin = giris.center(50,'*')
print(metin)

print("Uygulama başlıyor.")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go")



hak = int(input('Kaç kez Zar atmak istersiniz ? : '))

while hak > 0:
    bil_tahmin = random.randint(1,6)
    print('Devam etmek için "D" tuşuna basınız')
    devambutonu = input()
    if devambutonu == "d":
        hak -= 1
        print(f"***{bil_tahmin}*** ")
    else:
        print("yanlış tuşlama girdiniz")
    














