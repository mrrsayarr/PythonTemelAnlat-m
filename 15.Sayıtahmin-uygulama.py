'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
    buldurmaya çalışın. (hak = 5) olacak.
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanicıdan alın ve her soru belirtilen can sayısı
       üzerinden hesaplansın.
'''
 
import random

sayi = random.randint(1,10) #1 den  10 a kadar sayıları yazdırır.
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1 #Her seferinde kişinin hakkı 1 eksilir.
    sayac += 1
    tahmin = int(input('Tahmin: '))
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100 / can) * (sayac - 1)}')
        break
    elif sayi < tahmin:
        print('Sayı tahmininizden küçüktür...')
    elif sayi > tahmin:
        print('Sayı tahmininizden büyüktür...')
    else:
        print('Yanlış karakter girdiniz.')

    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')










