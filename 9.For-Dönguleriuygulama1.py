
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

from unicodedata import name


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir) #izmir rize çıktısını verir.


print('\n')
urunler = [
    {'name':'samsung S6' , 'price': '3000' },
    {'name':'samsung S7' , 'price': '4000' },
    {'name':'samsung S8' , 'price': '5000' },
    {'name':'samsung S9' , 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]
# 5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam ürün fiyatı:',toplam) #25000 yazdırır.

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urunfiyat in urunler:
    if int(urunfiyat['price']) <= 5000:
        print(urunfiyat['name'])
        # samsung S6
        # samsung S7
        # samsung S8
