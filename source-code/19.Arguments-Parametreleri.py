
from multiprocessing.sharedctypes import Value


def changename(n):
    n = 'ada'
name = 'yigit'
changename(name)
print(name) # yigit

def change1(n):
    n[0] = 'İstanbul' #ilk indise(0) 'İstanbul'u ata.
sehirler = ['Ankara', 'İzmir']

n = sehirler[:] #slicing işlemi yapıldı.
n[0] = 'İstanbul'

print(sehirler) # ['Ankara', 'İzmir']
print(n) # ['İstanbul', 'İzmir'] olarak yazar.

#**********************************************
def add(a, b, c = 0): # c=0 dememizin sebebi eğer c ye bir parametre atanmadıysa değeri 0 olsun.
    return sum((a, b, c))
print(add(10, 20)) # 30 çıktısını verir c=0 olarak alınmıştır
print(add(10, 20, 30)) # c yerine 30 atıyor.
#Bunun yerine alternatif olarak:
def add(*params):
    print(params) # Gönderilen tüm sayılar bir liste olarak yazdırılır. (Tuple listesi olarak)
    return(sum(params))
print(add(10, 20))
print(add(10,20,30,40,50,60)) # İstediğimiz kadar parametre atayabiliriz. (Çıktı: 210)
#*********************************************************************************************

def displayUser(**args): #2 yıldız dictionary(sözlük) olmasını sağlar. 
    for key, Value in args.items():
        print(type(args)) # <class 'dict'> 
        print('{} is {}'.format(key,Value))
            # name is Çınar
            # age is 2 ... gibi yazdırır
displayUser(name = 'Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Elif', age = 10, city = 'Sakarya', phone = '123456789')
displayUser(name = 'Mehmet', age = 15, city = 'Amasya', phone = '987987989', email = 'mehmet@gmail.com')


def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50, key1 = 'Value 1', key2 = 'Values 2')
        #10
        #20
        #(30, 40, 50)
        #{'key1': 'Value 1', 'key2': 'Values 2'}
