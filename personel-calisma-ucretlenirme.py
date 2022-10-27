# Fonksiyon nesne oluştururken isim, maas, rutbe değerlerinin alınmasını sağlıyor.
# Çalış fonksiyonu çağrılması ile personelin gün sayısı bir artıyor ve çalıştığı söyleniyor.
# Terfi fonksiyonu çağrılması ile personele atanan maaş değeri artıyor.(200)
# Bilgileri göster fonksiyonu çağrılması ile ekrana isim, maaş, toplam çalışılan gün sayısı, personelin rütbesi yazılıyor.

class Staffs:

    def __init__(self, name, maas, rutbe, gunsayisi):
        self.name = name
        self.maas = maas
        self.rutbe = rutbe
        self.gunsayisi = gunsayisi

    def calis(self):
        self.gunsayisi += 1
        return f"Çalıştığı gün sayısı {self.gunsayisi}"
    def terfi(self):
        self.maas += 200
        return f"Terfi aldınız yeni maaşınız {self.maas}"

    def bilgileriGoster (self):
        return f"Personel Ad - SOYAD: {self.name}, çalışan aldığı maaş: {self.maas}, çalıştığı gün sayısı: {self.gunsayisi}, personel rütbe: {self.rutbe} "
    
staf1 = Staffs("Şeref Kekeç", 1500, " Usta ", 200)
staf2 = Staffs("Ömer Faruk",2000, " Usta Başı ", 500)
staf3 = Staffs("Kayahan Bayazit",1000, " Çırak ", 0)

stafs = [staf1, staf2, staf3]


for s in stafs:
    print(s.bilgileriGoster())

        

                



















