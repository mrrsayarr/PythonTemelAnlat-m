# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir(kelime, adet):
    print(kelime * adet)
yazdir('Merhaba \n', 3) # 3 defa merhaba yazdırır.


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yaz.
def listeyeCevir(*args): # Sınırsız olması için * kullanımı önemlidir.
    liste = []

    for a in args:
        liste.append(a)
    
    return liste
result = listeyeCevir(10,20,30,7,8,9,6,6,3,2,6,3,4)
print(result) #[10, 20, 30, 7, 8, 9, 6, 6, 3, 2, 6, 3, 4]


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break #Eğer sayı asal değilse bırak.
#                 else:
#                     print(sayi) 
#                     break

# sayi1 = int(input('1. sayı: '))
# sayi2 = int(input('2. sayı: '))

# asalSayilariBul(sayi1, sayi2)


# 4- Kendisine gönderilen bir sayınıin tam bölenlerini bir liste şeklinde döndürür.
def tambolen(sayimiz):
    tambol = []
    for i in range(2, sayimiz):
        if sayimiz % i == 0:
            tambol.append(i)
    return tambol
print(tambolen(20)) #[2, 4, 5, 10]
