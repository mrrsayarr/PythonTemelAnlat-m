
sayilar = [1,3,5,7,9,12,19,21] 

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
for sayi0 in sayilar:
    if (sayi0 % 3 == 0):
        print(sayi0) #3 9 12 21 çıktısını verir.


# 2- Sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0
for sayi1 in sayilar:
    toplam += sayi1
print('Toplam: ',toplam) #77 değerini verir.
    

# 3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi2 in sayilar:
    if (sayi2 % 2 == 1): #Tek olduğunu anlmak için 2 bölümğnden kalan 1 olmalıdır.
        print(sayi2 ** 2) #1 9  25 49 81 361 441 çıktısını verir
