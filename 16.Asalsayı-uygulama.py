'''
Soru: Girilen sayının asal olup olmadığını bulunuz.
*** Asal sayı kendisi ve 1 dışında böleni olmayan sayılardır.
2, 3, 5, 7....
'''

sayi = int(input('Sayı girin: '))
asalmi = True

if sayi == 1:
    #print('1 Sayısı asal değildir.')
    asalmi = False
    1
for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('Sayı asaldır.')
else:
    print("Sayı asal değildir.")