
sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
# i = 0
# while(i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdıirın.
# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))
# i = baslangic
# while i < bitis:    #Bitişe kadar devam etsin.
#     i += 1          #Her seferinde 1 artar.
#     if i % 2 == 1:  #Tek sayıları yazdrımak için kullanılır.
#         print(i)    #Başlangıç değerden bitiş değerine kadar tüm sayıları yazar.


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# i = 100 #Normlade 0 dan 100 yazdırmak için i=0 olurdu tam tersi yazılacak
# while i > 0: 
#     print(i)
#     i -= 1 #Her defasında 1'azalır.


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda 'sıralı' bir şekilde yazdırın.
# numbers = []
# i = 0
# while i < 5:
#     sayi = int(input('Sayı: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort() #Sayıları küçükten büyüğe doğru sıralar.
# print(numbers) #Girilen sayıları :[10, 20, 30, 40, 50] şeklinde yazdırır.



# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#     ** ürün sayı1sını kullanıcıya sorun. 
#     ** dictionary listesi yapısı (name, price) şeklinde olsun.
#     ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler = []
adet = int(input('Kaç ürün eklemek istiyorsunuz: '))

i = 0
while(i < adet):
    name = input('Ürün ismi: ')
    price = int(input('Ürün fiyatı: '))
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'Ürün adı: {urun["name"]} Ürün fiyatı: {urun["price"]}')

# Kaç ürün eklemek istiyorsunuz: 2
# Ürün ismi: Ekmek
# Ürün fiyatı: 5
# Ürün ismi: Su
# Ürün fiyatı: 10
# Ürün adı: Ekmek Ürün fiyatı: 5
# Ürün adı: Su Ürün fiyatı: 10 


