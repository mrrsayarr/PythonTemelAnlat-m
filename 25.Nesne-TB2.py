#Classlar

from ctypes import addressof
class  Person:
    pass #Boş olması durumunda hata verir. Fakat pass keywordu ile boş alan doldurulmuş olur.

    # (class) attributes
    address = 'no information' #Her zaman kullanılmayacak özellikler class attributes adı altında belirtilir.
    #consturcator (yapıcı metot)
    def __init__(self, name, year): #self yerine başka bir parametre ismi konulabilir.
        # Önemli olan self parametresinin görevini yerine getirmesidir.
        # (object) attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.') # 2 defa init metodu çalıştı yazar.
        #methodlar

# if a > 10:
#     pass
#     Böylece bir şey yazmamıza gerek kalmaz.

# Object (instance)
p1 = Person(name = 'ali', year = 1990) #name : ali , year: 1990
p2 = Person('ayse', 1992) #name : ayse , year: 1992

#updating
p1.name = 'ahmet' # ali  ismi ahmet olarak değişir.
p1.address = 'kocaeli' # no information bilgisi kocaeli olarak yazdırılır.

#accessing object attributes
print(f'name: {p1.name} , year: {p1.year} , adres: {p1.address}.')
print(f'name: {p2.name} , year: {p2.year} , adres: {p2.address}')

print(p1) # <__main__.Person object at 0x0000021A5ED4AD10> yani bellekte p1 nesnesi için yer ayrıldı.
print(p2) #p2 tanımldanığı andan itibaren bellekte yer tahsisi yapılır.

print(type(p1)) # <class '__main__.Person'>
print(type(p2)) # <class '__main__.Person'>

print(p1 == p2) #False döndürür.
















