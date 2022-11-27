# name = 'Sadıkturan'

# for letter in name:
#     if letter  == 'ı': # 'ı' harfine kadar olan kısmı yazdırır.
#         break #Döngüyü kırma anlamına gelmektedir.
#     print(letter) #S a d harflerini yazar.

# for letter in name:
#     if letter  == 'ı': #'ı' görünce geç
#         continue 
#     print(letter) #S a d k t u r a n yazdırır ama 'ı' harfi olmaz.


# x = 0
# while x < 5:
#     if x == 2:
#         break #Eğer x 2'ye eşit ise döngüyü kır ve çık
#     print(x) #0 1 yazdırır.
#     x += 1
# while x < 5:
#     if x == 2:
#         continue    
#     print(x) #0 1 3 4 yazdırır.
#     x += 1

#1 den 100 e kadar tek sayıların toplamı
from unittest import result

result = 0
x = 1
while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x
print(f'Toplam: {result}') #Toplam: 2550 sonucunu verir.


