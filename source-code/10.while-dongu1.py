
#0-100 e kadar yazdırma

# x = 0

# while x <= 100: #100 e kadar (dahil) anlamına gelir.
#     if x % 2 == 0: #Koşul eklenebilir Burada sadece çift sayıları alır.
#         print(f'Sayı çifttir: {x}') #Ör: Sayı çifttir: 10
#     else:
#         print(f'Sayı tektir: {x}') #Ör: Sayı tektir: 11
#     x += 1 # x = x + 1 anlamına gelmekte ve her adımda 1 artar.

# print('Döngü bitti...')

name = '' #Boşlık False anlamına gelir.
#Eğer not name denilirse False ın değili yani True değer döner.

while not name.strip(): #Eğer isim girilmezse döngüye girer ve yazılana kadar bekler.
    #Boşluğu kontrol etmesi için strip() metodunu kullanabiliriz.
    name = input('İsminizi Girin: ')

print(f'Merhaba, {name}')
