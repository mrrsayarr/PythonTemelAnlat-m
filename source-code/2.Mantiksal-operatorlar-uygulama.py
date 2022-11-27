
# 1- Girilen bir sayınıin 0-100 arasında olup olmadığını kontrol ediniz.
# sayi = float(input('sayı: '))
# result = sayi > 0 and sayi <= 100 
# print(f'Sayı 0-100 arasında mı: {result}') #14 için==> Sayı 0-100 arasında mı: True çıktsını verir.
#**********************************************************************************
# 2- Girilen bir sayınıin pozitif sayı olup olmadığını kontrol ediniz.
# sayi = int(input('sayı: '))
# result = sayi > 0 and sayi % 2 == 0
# print(f'Girilen sayı çift sayı mı: {result}')
#**********************************************************************************
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = 'email@gmail.com'
# password = 'abc123'
# girilenmail = input('Email: ')
# girilenpassword = input('Password: ')
# result = (girilenmail == email) and (girilenpassword == password)
# print(f'Uygulamaya giriş başarılı mı: {result}')
#**********************************************************************************
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
from sys import float_info
from this import d
from typing import final
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# result = a>b and a>c
# print(f'a en büyük sayıdır: {result}')
# result = b>a and b>c 
# print(f'b en büyük sayıdır: {result}')
# result = c>a and c>b 
# print(f'c en büyük sayıdır: {result}')
#En büyük sayı True değeri döner geri kalanı ise False değeri döner.
#**********************************************************************************
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# vize1 = float(input('Vize 1: '))
# vize2 = float(input('Vize 2: '))
# final1 = float(input('Final: '))
# ortalama = (((vize1 + vize2)/2)*0.6 + final1*0.4)
# result = (ortalama > 49) and (final1 > 49)
# print(f'Ortalama: {ortalama} Geçme durumunuz: {result}')
#**********************************************************************************
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayı
#        Formül: (Kilo / boy uzunluğunun karesi)
#        Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#        0-18.4 => Zayıf
#        18.5-24.9 => Normal
#        25.0-29.9 => Fazla Kilolu
#        30.0-34.9 => Şişman (Obez)
name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: ')) #Boy 1.73 şeklinde yazılmalıdır.

index = (kg) / (hg ** 2)
zayif = index >= 0 and index <= 18.4
normal = index > 18.4 and index <= 24.9
kilolu = index > 24.9 and index <= 29.9
obez = index > 29.9 

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')
#Eğer Kilo:62 ve Boy:1.73 yazarsak normal: True olarak dönecektir.
























