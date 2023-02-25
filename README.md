
## Python Programlama Dili

- Python, genel amaçlı, yüksek seviyeli bir programlama dilidir. Python, okunması ve yazması kolay olan basit sözdizimi ile öne çıkar. Python açık kaynak kodludur ve tüm platformlarda (Windows, Linux, MacOS vb.) kullanılabilir.

## Değişkenler ve Veri Tipleri

Python'da herhangi bir değeri saklamak için değişkenler kullanılır. Değişkenlerin isimlendirilmesi için bazı kurallar vardır:

- Değişken ismi sayı ile başlayamaz.
- Değişken isimleri harf, sayı ve alt çizgi (_) içerebilir.
- Değişken isimleri büyük/küçük harf duyarlıdır.

Python'da kullanılan temel veri tipleri şunlardır:

- **Integer (Tam Sayı):** Tamsayılar, pozitif veya negatif tam sayılardır.
- **Float (Ondalık Sayı):** Ondalık sayılar, noktadan sonra rakamlar içeren sayılardır.
- **String (Metin):** Metinler, tek tırnak ('') veya çift tırnak ("") içinde yazılan karakter dizileridir.
- **Boolean (Mantıksal):** Mantıksal veri tipi, sadece True (Doğru) veya False (Yanlış) değerlerini alabilir.
##### Integer (Tam Sayı)

```
x = 5
y = -10
```
##### Float (Ondalık Sayı)
```
pi = 3.14
x = 2.5
```
##### String (Metin)
```
name = "Ali"
surname = 'Yılmaz'
```
##### Boolean (Mantıksal)
```
is_sunny = True
is_raining = False
```

## Koşullar ve Döngüler
Python'da koşullar ve döngüler, programların belirli şartlara göre çalışmasını sağlar.

- **If-Else Koşulu:** Belirli bir şart sağlandığında, programda belirli bir işlem yapılmasını sağlar. If-else koşulu, programlama dilinde temel yapı taşlarından biridir.
- **For Döngüsü:** Belirli bir sayıda tekrar etmek istediğimiz işlemleri gerçekleştirmek için kullanılır.
- **While Döngüsü:** Belirli bir şart sağlandığı sürece tekrar etmek istediğimiz işlemleri gerçekleştirmek için kullanılır.
##### If-Else Koşulu
```
x = 5

if x > 0:
    print("x pozitif")
else:
    print("x negatif veya sıfır")
```
##### For Döngüsü
```
for i in range(5):
    print(i)
```
##### While Döngüsü
```
i = 0

while i < 5:
    print(i)
    i += 1
```


## Fonksiyonlar
Fonksiyonlar, bir veya daha fazla işlemi gerçekleştirmek için kullanılan kod bloklarıdır. Fonksiyonlar, programlama dilinde modüler tasarımı sağlar ve kodun tekrar kullanılabilirliğini arttırır.
##### While Döngüsü
```
def greet(name):
    print("Merhaba, " + name)

greet("Ahmet")
```


## Nesne Tabanlı Programlama
Python, nesne tabanlı programlama (OOP) kavramlarını da destekler. OOP, programların daha kolay anlaşılır, yönetilebilir ve genişletilebilir hale getirilmesini sağlar.

##### OOP
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Merhaba, ben " + self.name)

p1 = Person("Ali", 25)
p1.greet()
```
### Çift / Tek Sayı Kontrolü
```
x = 7

if x % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")

print(x + y)
```
### Faktöriyel Hesaplama
```
n = 5
faktoriyel = 1

for i in range(1, n+1):
    faktoriyel *= i

print(faktoriyel)
```
### Asal Sayı Kontrolü
```
x = 7
asalMi = True

for i in range(2, x):
    if x % i == 0:
        asalMi = False
        break

if asalMi:
    print("Asal sayı")
else:
    print("Asal sayı değil")
```
### Liste Elemanları Toplamı
```
liste = [1, 2, 3, 4, 5]

toplam = 0
for eleman in liste:
    toplam += eleman

print(toplam)
```
### Kelime Ters Çevirme
```
kelime = "Python"

ters_kelime = ""
for harf in kelime:
    ters_kelime = harf + ters_kelime

print(ters_kelime)
```
### Sayı Tahmin Oyunu
```
import random

sayi = random.randint(1, 100)

while True:
    tahmin = int(input("Tahmininizi girin: "))

    if tahmin < sayi:
        print("Daha yüksek bir sayı söyleyin.")
    elif tahmin > sayi:
        print("Daha düşük bir sayı söyleyin.")
    else:
        print("Tebrikler! Sayıyı doğru tahmin ettiniz.")
        break
```
### Tekrar Eden Elemanları Bulma
```
liste = [1, 2, 3, 3, 4, 5, 5]

tekrarlar = []
for eleman in liste:
    if liste.count(eleman) > 1 and eleman not in tekrarlar:
        tekrarlar.append(eleman)

print(tekrarlar)
```
### Fibonacci Serisi
```
n = 10
fibonacci = [0, 1]

for i in range(2, n):
    sayi = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(sayi)

print(fibonacci)
```

# Nesne Tabanlı Programlama 
Python'da nesne tabanlı programlama kavramlarını kullanarak, daha anlaşılır, yönetilebilir ve genişletilebilir kodlar yazabiliriz. Bu bölümde, Python'da nesne tabanlı programlama kavramlarını örnek kod bloklarıyla açıklayacağız.

### Sınıflar ve Nesneler
Sınıflar, Python'da nesne tabanlı programlamanın temel yapı taşlarından biridir. Sınıflar, bir nesnenin özelliklerini (attributes) ve yöntemlerini (methods) tanımlayan bir çeşit şablon olarak düşünülebilir.
```
# Sınıf tanımı
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Yıl:", self.yil)

# Nesne oluşturma
araba1 = Araba("Renault", "Clio", 2015)

# Nesne yöntemlerine erişim
araba1.bilgileri_goster()
```
Yukarıdaki örnekte, Araba adında bir sınıf tanımladık. Sınıfın özellikleri marka, model ve yıl olarak tanımlandı. **init**() fonksiyonu, sınıftan nesne oluşturulduğunda özelliklerin nasıl tanımlanacağını belirler.

Ayrıca, sınıfın metodlarından biri olan bilgileri_goster() fonksiyonu, oluşturulan nesnenin özelliklerini ekrana yazdırır.

### Kalıtım
Kalıtım, nesne tabanlı programlamada bir sınıftan yeni bir sınıf oluşturma yöntemidir. Kalıtım sayesinde, bir sınıfın özelliklerini ve yöntemlerini başka bir sınıfın da kullanmasını sağlayabiliriz.
```
# Sınıf tanımı
class Hayvan:
    def __init__(self, isim, tur):
        self.isim = isim
        self.tur = tur

    def bilgileri_goster(self):
        print("İsim:", self.isim)
        print("Tür:", self.tur)

# Kalıtım alınan sınıf
class Kedi(Hayvan):
    def miyavla(self):
        print("Miyav!")

# Nesne oluşturma
kedi1 = Kedi("Tekir", "Siyam")

# Kalıtım alınan sınıfın yöntemlerine erişim
kedi1.bilgileri_goster()

# Kendi yöntemlerine erişim
kedi1.miyavla()
```
Yukarıdaki örnekte, Hayvan adında bir sınıf tanımladık. Bu sınıfın özellikleri isim ve tür olarak tanımlandı. **init**() fonksiyonu, sınıftan nesne oluşturulduğunda özelliklerin nasıl tanımlanacağını belirler.

Kedi adında bir sınıf oluşturduk ve bu sınıf, Hayvan sınıfından kalıtım aldı. Kedi sınıfı, Hayvan sınıfının özelliklerini ve yöntemlerini kullanabilir. Ayrıca, Kedi sınıfına, miyavla() adında bir yöntem ekledik.

### Polimorfizm
Polimorfizm, nesne tabanlı programlamada aynı adı taşıyan ancak farklı işlevleri olan yöntemlerin kullanımıdır. Polimorfizm, bir sınıfın farklı durumlarda farklı işlevler görebilmesini sağlar.
```
# Sınıf tanımı
class Sekil:
    def alan_hesapla(self):
        pass

# Alt sınıflar
class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

class Ucgen(Sekil):
    def __init__(self, taban, yukseklik):
        self.taban = taban
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return (self.taban * self.yukseklik) / 2

# Nesne oluşturma
sekil1 = Dikdortgen(5, 10)
sekil2 = Ucgen(8, 6)

# Polimorfizm
sekil_listesi = [sekil1, sekil2]

for sekil in sekil_listesi:
    print(sekil.alan_hesapla())
```
Yukarıdaki örnekte, Sekil adında bir sınıf tanımladık. Bu sınıf, alan_hesapla() adında bir yöntem içeriyor. Ancak bu yöntem, henüz tanımlanmadı.

Dikdortgen ve Ucgen adında iki alt sınıf oluşturduk. Her iki alt sınıf da Sekil sınıfından kalıtım aldı ve alan_hesapla() yöntemini farklı şekillerde tanımladı.

Nesne oluşturduktan sonra, Dikdortgen ve Ucgen nesnelerini sekil_listesi adında bir liste içinde topladık. Ardından, bu liste üzerinde bir döngü oluşturarak, her nesnenin alanını hesaplayıp ekrana yazdırdık. Bu işlem sırasında, polimorfizm özelliğinden yararlandık.

Yukarıdaki örnekler, Python'da nesne tabanlı programlama kavramlarını örnek kod bloklarıyla açıklamaktadır. Nesne tabanlı programlama, kodların daha anlaşılır, yönetilebilir ve genişletilebilir hale getirilmesini sağlar.

 
 
 
 
 
 
 
 
 

## Python Temel Konu
Bu Repo konu anlatmaya yönelik bir Repo'dur. 
Sadık Turan sayesinde öğrendiğim ve faydalı gördüğüm Python dosyalarını, alakalı linkleri buraya atmaya çalışacağım.

Geniş bir şekilde konuyu öğrenmek için güzel kaynak:

### https://python-istihza.yazbel.com/

### https://github.com/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama

### https://python-ogren.readthedocs.io/en/latest/intro.html

### https://riptutorial.com/python

### https://aktif.net/python-programlama/

Hem ingilizce hem de python bilgisi için çok yararlı kaynak:

### https://www.w3schools.com/python/default.asp


```
x = 6
result = 5 < x < 10 #True değeri döner.

#ve

result = x > 5 and x < 10 #True

#veya

result = x > 5 or x % 2 == 0 #True, and olursa False olur.

#not

result = not(x > 5) #False 

#x, 5-10 arasında olan bir çift sayı mı?

result = x > 5 and x < 10 and x % 2 == 0 #True döner
result = x < 5 and x < 10 and x % 2 == 0 #False döner

print(result)
```


1- Girilen bir sayınıin 0-100 arasında olup olmadığını kontrol ediniz.
```
sayi = float(input('sayı: '))
result = sayi > 0 and sayi <= 100 
print(f'Sayı 0-100 arasında mı: {result}') #14 için==> Sayı 0-100 arasında mı: True çıktsını verir.
```


2- Girilen bir sayınıin pozitif sayı olup olmadığını kontrol ediniz.
```

```
sayi = int(input('sayı: '))
result = sayi > 0 and sayi % 2 == 0
print(f'Girilen sayı çift sayı mı: {result}')

3- Email ve parola bilgileri ile giriş kontrolü yapınız.
```
email = 'email@gmail.com'
password = 'abc123'
girilenmail = input('Email: ')
girilenpassword = input('Password: ')
result = (girilenmail == email) and (girilenpassword == password)
print(f'Uygulamaya giriş başarılı mı: {result}')
```


4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
```
from sys import float_info
from this import d
from typing import final

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = a>b and a>c
    print(f'a en büyük sayıdır: {result}')
result = b>a and b>c 
    print(f'b en büyük sayıdır: {result}')
result = c>a and c>b 
    print(f'c en büyük sayıdır: {result}')
#En büyük sayı True değeri döner geri kalanı ise False değeri döner.
```

**********************************************************************************
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın
```
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır
b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final1 = float(input('Final: '))
ortalama = (((vize1 + vize2)/2)*0.6 + final1*0.4)
result = (ortalama > 49) and (final1 > 49)
print(f'Ortalama: {ortalama} Geçme durumunuz: {result}')
```
**********************************************************************************
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayı
       Formül: (Kilo / boy uzunluğunun karesi)
       Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
       0-18.4 => Zayıf
       18.5-24.9 => Normal
       25.0-29.9 => Fazla Kilolu
       30.0-34.9 => Şişman (Obez)
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
Eğer Kilo:62 ve Boy:1.73 yazarsak normal: True olarak dönecektir.

**********************************************************************************

##Identify Operator: is
#x = y = [1, 2, 3]
#z = [1, 2, 3]

#print(x==y) #True
#print(x==z) #True

#print(x is y) #True değer döner
#print(x is z) #False değer döner  çünkü değerlere bakmaz x ve y nin kendisine bakar.

x =[1,2,3]
y =[2,4]

del x[2] #x içindeki 3 silinir.
y[1] = 1 #y içindeki 4 1 olarak değişir.
y.reverse()

print (x==y) #True değeri döner çünkü elemanları x değerlerine çevirdik.
print(x is y) #False değer döner.   

#Membership Operator: in
x = ['apple', 'banana']
print('banana' in x) #'banana' liste içinde var mı: True değerini döner.

name = 'Çınar'
print('a' in name) #True döner yani 'a' değeri Çınar içerisinde bulunur.
print('a' not in name) #False değerini döner 'a' değeri Çınar stringinde bulunur.

**********************************************************************************
if 3 > 2:
     print('HoşGeldin...') #Yazar.

if 3 > 3:
     print('HoşGeldin...') #False olduğu için yazdıramaz.

isLoggedin = True
if isLoggedin:
     print('aaaa') #'aaaa' değerini döndürür. Fakat 'False' yaparsak değer dönmez.


**********************************************************************************


username = 'memo'
password = '1234'

isLoggedin = username=='memoo' and password=='1234'#Yanlış yazdırdık


if isLoggedin:
    print('Şifre Doğru hoşgeldin.') #Hatalı bilgiler girilince burayı atlar.
else:
    print('Bilgileriniz yanlış') #Hatalı bilgiler olduğu için burayı basar.

**********************************************************************************

if (username=='memo') and (password=='1234'): #Kullanıcı adı ve şifre dpğru ise print içindeki ifadeyi basar.
    print('Şifre Doğru hoşgeldin.')

#Eğer kullanıcı Hangisinin doğru olmadığını öğrenmek isterse  
if (username=='memo'):
    if (password =='1234'):
        print('Şifre ve Kullanıcı adı doğru.') #Kullanıcı adı ve Parola doğru ise bu bloğu yazdırır.
    else:
        print('Parolanız yanlış.') #Parola eğer yanlış olursa bir  if 'password' bloğuna geçer ve else bloğu çalışır. 


**********************************************************************************
x = int(input('x: '))
y = int(input('y: '))

if x > y:
    print('x y den büyük') #10 a 9 girilince if bloğu çalışır.
elif x==y:
    print('x y eşit') #9 a 9 değerler girilince elif bloğu çalışır.
else:
    print('y x den büyük') #8 a 9 girilince else bloğu çalışır.

**********************************************************************************

num = int(input('sayı: '))

if num > 0:
    print('Sayı pozitif') #(20) girilince bu blok çalışır
elif num < 0:
    print('Sayı Negatif') #(-20) girilince bu blok çalışır
else:
    print('Sayı sıfır') #(0) girilince bu blok çalışır


**********************************************************************************

#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve eğitim durumu
#lise ya da üniversite olmalıdır. 
from unicodedata import name


isim = input('isminiz: ')
yas = int(input('Yaşınız: '))
egitim = input('Eğitim: ')

#if (yas > 18) and (egitim == 'lise' or egitim =='üniversite'):
#  print('Ehliyet alabilirsiniz.') #Yaş 18 den büyük ve eğitimin lise veya üniversite olması gerekmektedir.
#else:
#  print('Ehliyet alamazsınız.')

#Ehliyetin neyden dolayı alınamadığını öğrenmek için
if (yas > 18):
     if (egitim == 'lise' or egitim =='üniversite'):
        print(f'{isim} Ehliyeti alabilirsin.') #Yaş 18 den büyük ve eğitimin lise veya üniversite olması gerekmektedir.
     else: 
         print(f'{isim} Eğitim durumunuzdan dolayı ehliyet alamazsın.')
else:   
     print(f'{isim} yaşınızdan dolayı ehliyet alamazsınız.')
 

**********************************************************************************

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#  not aralığına karşılık gelen not bilgisini yazdırınız.
#  0 - 24 => 0
#  25-44 => 1
#  45-54 => 2
#  55-69 => 3
#  70-84 => 4
#  3 85-100 => 5
yazili1 = int(input('1.Yazılı: '))
yazili2 = int(input('2.Yazılı: '))
sozlu = int(input('Sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu)/3

if ortalama >= 0 and ortalama < 25:
    print(f'Ortalamanız : {ortalama} notunuz: 0')
elif ortalama >=25 and ortalama < 45:
    print(f'Ortalamanız : {ortalama} notunuz: 1')
elif ortalama >=45 and ortalama < 54:
    print(f'Ortalamanız : {ortalama} notunuz: 2')
elif ortalama >= 55 and ortalama < 69:
    print(f'Ortalamanız : {ortalama} notunuz: 3')
elif ortalama >= 70 and ortalama < 84:
    print(f'Ortalamanız : {ortalama} notunuz: 4')
elif ortalama >= 85 and ortalama <=100:
    print(f'Ortalamanız : {ortalama} notunuz: 5')
else:
    print('Yanlış bilgi girdiniz.')


**********************************************************************************

#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
# göre hesaplayinız.
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
#   ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız      
#   *** datetime modülünü kullanmanız gerekiyor.
#  (simdi) - (2018/8/1) => gün
import datetime #Modül Kullanma

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
#print(tarih[0]) #2019
#print(tarih[1]) #8
#print(tarih[2]) #9 oalrak yazdırır.

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now() #datetime.now() modülü kodun derlendiği anın saat ve tarihini yazdırır.
fark = simdi - trafigecikis #Aradan geçen zamanın ne kadar olduğunu hesaplamak için farkı alındı.
days = fark.days

if days <= 365:
    print('1.Servis Aralığı ')
elif days > 365 and days <= 365*2:
    print('2.Servis Aralığı ')
elif days > 365*2 and days <= 365*3:
    print('3.Servis Aralığı')
else: 
    print('Hatalı süre') #Eğer girilen süre üzerinden 365*3 gün geçerse bunu yazar.

**********************************************************************************
'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
    
'''
sayi = float(input('sayı: '))
result = (sayi > 0) and (sayi<=100)

if result:
    print(f'Sayı 0-100 arasındadır.')
else:
    print('Sayı 0-100 arasında değildir.')



**********************************************************************************
'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

'''
sayi = int(input('sayı: '))
result = (sayi > 0) and (sayi % 2 ==0)

if (sayi > 0):
    if (sayi % 2 ==0):
        print(f'Girilen sayı pozitif çift sayıdır.')
    else:
        print('Girilen sayı tektir.')

elif sayi < 0 and sayi % 2 ==0:
    print('Sayı negatift çift sayıdır.')

else: 
    print('Sayı çift değildir.')

**********************************************************************************
'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız.

'''
email = 'email@gmail.com'
password = 'abc123'

girilenemail = input('Email: ')
girilenpassword = input('Password: ') 
                              
result = (girilenemail == email) and (girilenpassword == password)

if (girilenemail == email):
    if (girilenpassword == password):
        print(f'Uygulamaya giriş başarılı.')
    else:
        print('Yanlış Parola girdiniz.')
else:
    print(f'Email bilgisi yanlış')

**********************************************************************************
'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
    print(f'a en büyük sayıdır.')

elif (b > a) and (b > c):
    print(f'b en büyük sayıdır.')

elif (c > a) and (c > b):
    print(f'c en büyük sayıdır.')

else:
    print('Yanlış değer girdiniz.')

**********************************************************************************

'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.


'''
vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : ')) 

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

#result = (ortalama>=50) and (final>=50)
#result = (ortalama >=50) or (final>=70)

if ortalama >= 50:
    if final >= 50:
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı.')
    else:
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız.')
else:
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız.')

**********************************************************************************
numbers = [1,2,3,4,5]

#Eğer for döngüsü olmasaydı bunların hepsini elle yazmak zorunda kalacaktık.
#print(numbers[0]) #1
#print(numbers[1]) #2
#print(numbers[2]) #3
#print(numbers[3]) #4
#print(numbers[4]) #5 çıktılarını verirler 
for num in numbers:
    print(num) #Yine aynı çıktıyı verir. Daha kısa.



names = ['çınar', 'sadık', 'sena']
for name in names:
    print(f'My name is {name}') #Tüm isimleri cümle ile birlikte yazar.

name = 'ABCDEF'
for n in name:
    print(n)  #name stringini harf harf yazdırır.
    #Her eleman bir dizi eleman olarak yazdırılır.

tuple = (1,2,3,4,5)
for t in tuple:
    print(t) #Aynı şekilde Yazdırılır.
    #Hatırlatma: "Tuple içinde değişiklik yapılamaz."

tuples = [(1,2),(3,4),(5,6)]
for x,y in tuples:
    print(x) 
    #(1, 2)
    #(3, 4)
    #(5, 6) olarak çıktı verir.

d = {'k1':1, 'k2':2, 'k3':3}
for item in d.items():
    print(item) 
    #('k1', 1)
    #('k2', 2)
    #('k3', 3)
for key,value in d.items():
    print(key,value)
    #k1 1
    #k2 2
    #k3 3 

**********************************************************************************

sayilar = [1,3,5,7,9,12,19,21] 

#1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
for sayi0 in sayilar:
    if (sayi0 % 3 == 0):
        print(sayi0) #3 9 12 21 çıktısını verir.


#2- Sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0
for sayi1 in sayilar:
    toplam += sayi1
print('Toplam: ',toplam) #77 değerini verir.
    

#3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi2 in sayilar:
    if (sayi2 % 2 == 1): #Tek olduğunu anlmak için 2 bölümğnden kalan 1 olmalıdır.
        print(sayi2 ** 2) #1 9  25 49 81 361 441 çıktısını verir

**********************************************************************************

#4- Şehirlerden hangileri en fazla 5 karakterlidir ?

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
#5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam ürün fiyatı:',toplam) #25000 yazdırır.

#6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urunfiyat in urunler:
    if int(urunfiyat['price']) <= 5000:
        print(urunfiyat['name'])
        #samsung S6
        #samsung S7
        #samsung S8

**********************************************************************************

#0-100 e kadar yazdırma

#x = 0

#while x <= 100: #100 e kadar (dahil) anlamına gelir.
#  if x % 2 == 0: #Koşul eklenebilir Burada sadece çift sayıları alır.
#      print(f'Sayı çifttir: {x}') #Ör: Sayı çifttir: 10
#  else:
#      print(f'Sayı tektir: {x}') #Ör: Sayı tektir: 11
#  x += 1 #x = x + 1 anlamına gelmekte ve her adımda 1 artar.

#print('Döngü bitti...')

name = '' #Boşlık False anlamına gelir.
#Eğer not name denilirse False ın değili yani True değer döner.

while not name.strip(): #Eğer isim girilmezse döngüye girer ve yazılana kadar bekler.
    #Boşluğu kontrol etmesi için strip() metodunu kullanabiliriz.
    name = input('İsminizi Girin: ')

print(f'Merhaba, {name}')
**********************************************************************************
sayilar = [1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazdırın.
#i = 0
#while(i < len(sayilar)):
#  print(sayilar[i])
#  i += 1

#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdıirın.
#baslangic = int(input('Başlangıç: '))
#bitis = int(input('Bitiş: '))
#i = baslangic
#while i < bitis:    #Bitişe kadar devam etsin.
#  i += 1          #Her seferinde 1 artar.
#  if i % 2 == 1:  #Tek sayıları yazdrımak için kullanılır.
#      print(i)    #Başlangıç değerden bitiş değerine kadar tüm sayıları yazar.


#3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
#i = 100 #Normlade 0 dan 100 yazdırmak için i=0 olurdu tam tersi yazılacak
#while i > 0: 
#  print(i)
#  i -= 1 #Her defasında 1'azalır.


#4: Kullanıcıdan alacağınız 5 sayıyı ekranda 'sıralı' bir şekilde yazdırın.
#numbers = []
#i = 0
#while i < 5:
#  sayi = int(input('Sayı: '))
#  numbers.append(sayi)
#  i += 1
#numbers.sort() #Sayıları küçükten büyüğe doğru sıralar.
#print(numbers) #Girilen sayıları :[10, 20, 30, 40, 50] şeklinde yazdırır.



#5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#  ** ürün sayı1sını kullanıcıya sorun. 
#  ** dictionary listesi yapısı (name, price) şeklinde olsun.
#  ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
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

#Kaç ürün eklemek istiyorsunuz: 2
#Ürün ismi: Ekmek
#Ürün fiyatı: 5
#Ürün ismi: Su
#Ürün fiyatı: 10
#Ürün adı: Ekmek Ürün fiyatı: 5
#Ürün adı: Su Ürün fiyatı: 10 

**********************************************************************************

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

**********************************************************************************
for item in range(5,10): #5'ten başla 10 a kadar yazdır. 
    #Artış miktarı için bir virgül daha atıp istediğiniz sayıyı yazabilirsiniz.
    print(item)

for item in range(50,100,20):
    print(item)

print(list(range(50,100,20))) #Liste şeklinde yazdırır. 
 

**********************************************************************************

#index = 0
#greeting = 'Hellothere'

#for letter in greeting:
#  print(f'index: {index} letter: {greeting[index]}') #Indexleri yazdırır.
#  index += 1
#print("\n")
#for index,letter in enumerate(greeting):
#  print(f'index: {index} letter: {letter}') #Indexleri yazdırır. Yukardaki örneğin benzeri.
#  #index: 0 letter: H
#  #index: 1 letter: e
#  #index: 2 letter: l ... gibi yazdırır.
#print("\n")
#for item in enumerate(greeting):
#  print(item)
#  #(0, 'H')
#  #(1, 'e')
#  #(2, 'l') ... gibi yazdırır.
#print("\n")
#for index, item in enumerate(greeting):
#  print(f'index: {index} letter: {item}')

print("\n")
#zip metodu
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
#Liste sayısı arttırılabilir. (Benzer şekilde)
print(list(zip(list1,list2))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] olarak yazar.
print("\n")
for item in zip(list1, list2):
    print(item)
    #(1, 'a')
    #(2, 'b')... olarak çıktı verir.

print("\n")
for a,b in zip(list1, list2):
    print(a,b)
    #1 a
    #2 b
    #3 c
    #4 d... olaak çıktı verir.

**********************************************************************************

numbers = []
for x in range(10):
    numbers.append(x)
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] olarak yazar.

print("\n")
numbers = [x for x in range(10)]
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] olarak yazar.


print("\n")
for c in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] olarak yazar.

print("\n")
numbers = [x*x for x in range(10) if x%3==0]
print(numbers) #[0, 9, 36, 81] olarak yazdırır.

print("\n")
myString = 'Hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)  #['H', 'e', 'l', 'l', 'o'] olarak yazar.


print("\n")
years = [1983,1999,2008,1956,1986]
ages = [2019-year for year in years]
print(ages) #[36, 20, 11, 63, 33] olarak değerleri döner.

results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results) #['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK'] 

print("\n")
result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result) 
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print("\n")
#Yukardaki kod ile aynı cevabı verir.
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#x y yanında z olarak kullanılabilir çıktısı (x, y, z) şeklinde olur.

**********************************************************************************
'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
    buldurmaya çalışın. (hak = 5) olacak.
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanicıdan alın ve her soru belirtilen can sayısı
       üzerinden hesaplansın.
'''
 
import random

sayi = random.randint(1,10) #1 den  10 a kadar sayıları yazdırır.
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1 #Her seferinde kişinin hakkı 1 eksilir.
    sayac += 1
    tahmin = int(input('Tahmin: '))
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100 / can) * (sayac - 1)}')
        break
    elif sayi < tahmin:
        print('Sayı tahmininizden küçüktür...')
    elif sayi > tahmin:
        print('Sayı tahmininizden büyüktür...')
    else:
        print('Yanlış karakter girdiniz.')

    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')


**********************************************************************************
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

**********************************************************************************

#metodlar
list = [1,2,3]

list.append(4) #[1,2,3,4]
#append bir metottur ve listeye 4 ekler

list.pop() #[1,2,3]
#pop da bir metottur ve listenin sonundaki eleman silinir.

print(type(list)) #<class 'list'>
print(list) 

myString= 'Hello'

print(type(myString)) #<class 'list'>
print(myString.upper()) #HELLO

'''
METOT-FONKSİYON FARKI

Sonuç olarak fonksiyon ve metotlar; kodların tekrar 
kullanılabilirliğini sağlamaktadır. Fonksiyonlar, 
kullanıcı tarafından tanımlanabileceği gibi Python'da 
hazır olarak da tanımlanmıştır. Metotlar ise sadece sınıf 
içinde tanımlanımlanırken örneklem üzerinden metotlara 
ulaşabiliriz.
'''

**********************************************************************************

#def demek o parçanın fonkiyon olduğu anlamına gelir.

#def sayHello(name):
#  print('Hello ' + name)
#sayHello('Çınar') #Hello Çınar çıktısını verir.


def sayHello(name = 'user'):
    return 'Hello ' + name
msg = sayHello('Çınar') #Hello Çınar yazdırır.
print(msg)

def total(num1, num2):
    return num1 + num2 
result = total(10,20)
print(result) #30 çıktısını verir.

def yasHesapla(dogumyili):
    return 2019 - dogumyili
agecinar = yasHesapla(2015)
ageada   = yasHesapla(2010)
print(agecinar, ageada) #4 9 sonçlarını verir.

def emeklilignekadarkaldı(dogumyili, isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı ')
    else:
        print('zaten emekli oldunuz.')
emeklilignekadarkaldı(1983, 'Ali') #Emekliliğinize 29 yıl kaldı
emeklilignekadarkaldı(1950, 'Ali') #Zaten emekli oldunuz.

print(help(emeklilignekadarkaldı)) 
    #DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    #INPUT: Doğum yılı
    #OUTPUT: Hesaplanan yıl bilgisi

list = [1,2,3]
print(help(list.append)) #Ekleme yapılabileceğini söylüyor.

**********************************************************************************
from multiprocessing.sharedctypes import Value


def changename(n):
    n = 'ada'
name = 'yigit'
changename(name)
print(name) #yigit

def change1(n):
    n[0] = 'İstanbul' #ilk indise(0) 'İstanbul'u ata.
sehirler = ['Ankara', 'İzmir']

n = sehirler[:] #slicing işlemi yapıldı.
n[0] = 'İstanbul'

print(sehirler) #['Ankara', 'İzmir']
print(n) #['İstanbul', 'İzmir'] olarak yazar.

********************************
def add(a, b, c = 0): #c=0 dememizin sebebi eğer c ye bir parametre atanmadıysa değeri 0 olsun.
    return sum((a, b, c))
print(add(10, 20)) #30 çıktısını verir c=0 olarak alınmıştır
print(add(10, 20, 30)) #c yerine 30 atıyor.
#Bunun yerine alternatif olarak:
def add(*params):
    print(params) #Gönderilen tüm sayılar bir liste olarak yazdırılır. (Tuple listesi olarak)
    return(sum(params))
print(add(10, 20))
print(add(10,20,30,40,50,60)) #İstediğimiz kadar parametre atayabiliriz. (Çıktı: 210)

***********

def displayUser(**args): #2 yıldız dictionary(sözlük) olmasını sağlar. 
    for key, Value in args.items():
        print(type(args)) #<class 'dict'> 
        print('{} is {}'.format(key,Value))
            #name is Çınar
            #age is 2 ... gibi yazdırır
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

**********************************************************************************

#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir(kelime, adet):
    print(kelime * adet)
yazdir('Merhaba \n', 3) #3 defa merhaba yazdırır.


#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yaz.
def listeyeCevir(*args): #Sınırsız olması için * kullanımı önemlidir.
    liste = []

    for a in args:
        liste.append(a)
    
    return liste
result = listeyeCevir(10,20,30,7,8,9,6,6,3,2,6,3,4)
print(result) #[10, 20, 30, 7, 8, 9, 6, 6, 3, 2, 6, 3, 4]


#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
#def asalSayilariBul(sayi1, sayi2):
#  for sayi in range(sayi1, sayi2 + 1):
#      if sayi > 1:
#          for i in range(2, sayi):
#              if sayi % i == 0:
#                  break #Eğer sayı asal değilse bırak.
#              else:
#                  print(sayi) 
#                  break

#sayi1 = int(input('1. sayı: '))
#sayi2 = int(input('2. sayı: '))

#asalSayilariBul(sayi1, sayi2)


#4- Kendisine gönderilen bir sayınıin tam bölenlerini bir liste şeklinde döndürür.
def tambolen(sayimiz):
    tambol = []
    for i in range(2, sayimiz):
        if sayimiz % i == 0:
            tambol.append(i)
    return tambol
print(tambolen(20)) #[2, 4, 5, 10]

**********************************************************************************

#Map-Filter

import numbers


def square(num): return num ** 2

numbers1 = [1, 3, 5, 7, 4, 6]

result = list(map(square, numbers1))
#map metodu bellektki adresi verir. Fakat list ile yazdırırsak bize numebrs listesini çağırır.
for item in map(square, numbers1):
    print(item)

#Veya başka bir kullanım yolu da

numbers2 = [2, 4, 6, 8]
result = list(map(lambda num: num ** 2, numbers2))
print(result) #[4, 16, 36, 64] olarak çıktı verecektir.

******************************
numbers1 = [1, 3, 5, 7, 4, 6]

def check_even(num): return num % 2 == 0
result = list(filter(check_even, numbers1))
print(result) #[4, 6] olarak yazar.

#Veya

result = list(filter(lambda num: num%2==0, numbers1))
print(result)

#Ya da

check_even = lambda num: num%2==0
result = check_even(numbers[2])#Sayı tek olduğu için False bilgisini döner.
print(result)


**********************************************************************************

name = 'Ali'

def changename(newname):
    name = newname
    print(name) #Memo

changename('Memo')
print(name) #Ali

#############################

name = 'Global String'
def greeting():
    #name = 'Ali' -- Yorum satırı kaldırılırsa hello Ali yazar.

    def hello():
        print('Hello' + name)
    
    hello()
greeting()
#hello Global String i yazdırır.

#############################

x = 50
def test():
    global x
    
    print(f'x: {x}')

    x = 100
    print(f'Changed x to {x}')
test()
print(x)
    #x: 50 (global x yazılırsa)
    #Changed x to 100 (global x yazılırsa)
    #100 (global x yazılırsa)

#############################
x = 50
def test(x):
    print(f'x: {x}')

    x = 100
    print(f'Changed x to {x}')
test(x)
print(x)
    #x: 50
    #Changed x to 100
    #50

**********************************************************************************


AliHesap = {
    'ad': 'Ali Pala',
    'hesapNo': '11111111',
    'bakiye': 3000,
    'ekHesap': 2000
}
AyseHesap = {
    'ad': 'Ayse Pala',
    'hesapNo': '22222222',
    'bakiye': 200,
    'ekHesap': 1000
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar :
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesaptan para çekilsin mi ? (e/h)')
            
            if ekHesapKullanimi == 'e':
                bakiye = hesap['bakiye']
                ekhesapkulllanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapkulllanilacakmiktar
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        
        else:
            print('Üzgünüm bakiyeniz yetersiz.')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır. ")



paraCek(AliHesap, 3000)
bakiyeSorgula(AliHesap)

print(' *****************')

paraCek(AliHesap, 2000)


**********************************************************************************


#object Orianted Programming (OOP)
#Class
#instance --> Object

list1 = [1,2,3,4]
list2 = [1,2,3,4,5]

result = type(list1)
print(result) #<class 'list'>

result = type(list2) #List1 bir için ne olduğunu class ifadesi ile verir.
print(result) #<class 'list'>

**********************************************************************************

#Classlar

from ctypes import addressof
class  Person:
    pass #Boş olması durumunda hata verir. Fakat pass keywordu ile boş alan doldurulmuş olur.

    #(class) attributes
    address = 'no information' #Her zaman kullanılmayacak özellikler class attributes adı altında belirtilir.
    #consturcator (yapıcı metot)
    def __init__(self, name, year): #self yerine başka bir parametre ismi konulabilir.
        #Önemli olan self parametresinin görevini yerine getirmesidir.
        #(object) attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.') #2 defa init metodu çalıştı yazar.
        #methodlar

#if a > 10:
#  pass
#  Böylece bir şey yazmamıza gerek kalmaz.

#Object (instance)
p1 = Person(name = 'ali', year = 1990) #name : ali , year: 1990
p2 = Person('ayse', 1992) #name : ayse , year: 1992

#updating
p1.name = 'ahmet' #ali  ismi ahmet olarak değişir.
p1.address = 'kocaeli' #no information bilgisi kocaeli olarak yazdırılır.

#accessing object attributes
print(f'name: {p1.name} , year: {p1.year} , adres: {p1.address}.')
print(f'name: {p2.name} , year: {p2.year} , adres: {p2.address}')

print(p1) #<__main__.Person object at 0x0000021A5ED4AD10> yani bellekte p1 nesnesi için yer ayrıldı.
print(p2) #p2 tanımldanığı andan itibaren bellekte yer tahsisi yapılır.

print(type(p1)) #<class '__main__.Person'>
print(type(p2)) #<class '__main__.Person'>

print(p1 == p2) #False döndürür.

**********************************************************************************



#Classlar

from ctypes import addressof
class  Person:
    pass #Boş olması durumunda hata verir. Fakat pass keywordu ile boş alan doldurulmuş olur.

    #(class) attributes
    address = 'no information' #Her zaman kullanılmayacak özellikler class attributes adı altında belirtilir.
    #consturcator (yapıcı metot)
    def __init__(self, name, year): #self yerine başka bir parametre ismi konulabilir.
        #Önemli olan self parametresinin görevini yerine getirmesidir.
        #(object) attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('Hello there. I am ' + self.name) #Hello there. I am ali
  
    #instance methods
    def calculateAge(self):
        return 2019 - self.year

#Object (instance)
p1 = Person(name = 'ali', year = 1990) #name : ali , year: 1990
p2 = Person('ayse', year = 1992) #name : ayse , year: 1992

p1.intro() #Hello there. I am ali
p2.intro() #Hello there. I am ayse

print(f'Adım: {p1.name} ve Yaşım: {p1.calculateAge()}') #Adım: ali ve Yaşım: 29 
print(f'Adım: {p2.name} ve Yaşım: {p2.calculateAge()}') #Adım: ayse ve Yaşım: 27

**********************************************************************************



class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)


c1 = Circle() #Yaiçap belirtilmezse oto 1 alınır.
c2 = Circle(5)

print(f'c1 : alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}') #c1 : alan = 3.14 çevre = 6.28
print(f'c2 : alan = {c2.alanHesapla()} çevre = {c2.cevreHesapla()}') #c2 : alan = 78.5 çevre = 31.400000000000002

**********************************************************************************


#Inheritance (Kalıtım): Miras  ALma
 
#Person => name, lastname, age, eat(), run(), drink()
#Student, Teacher da olmasını isteriz
#Bu yzüden Studen(Person), Teacher(Person) ile Person Sınıfını miras alırız.

#Ya da 

#Animal => Dog(Animal), Cat(Animal) gibi ...

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person created')

    def who_am_i(self):
        print('I am a Person :(')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self,fname,lname)
        self.studentnumber = number
        print('Student created')

    #override
    def who_am_i(self): #Yukarıda ki fonksiyonu ezmek (override etmek) için kullanıldı
        print('I am a Student :)') #Override edilen fonka yazılan yeni Metin

    def sayhello(self):
        print('Helllo I am a STUDENT')
        
class Teacher(Person):
    def __init__(self,fname,lname, branch):
        super().__init__(fname,lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} TEACHER')
        

t1 = Teacher('Serkan','Arı','SOFTWARE')
p1 = Person('Mehmet', 'Ata')
s1 = Student('Ali', 'Bşaran','12356') #number sadece Student'a özel olduğu için sadece burda yazılabilir
#Person created
#Student created - Miras  alıyor

print(p1.firstname + ' ' + p1.lastname) #Mehmet Ata
print(s1.firstname + ' ' + s1.lastname + ' ' + s1.studentnumber) #Ali Bşaran 12356

t1.who_am_i() #I am a SOFTWARE TEACHER
p1.who_am_i() #I am a Person
s1.who_am_i() #I am a Person

p1.eat() #I am eating
s1.eat() #I am eating

s1.sayhello() #Hello I am a STUDENT "Sadece Student'a ait bir yapıdır"



**********************************************************************************

mylist = [1,2,3]
mystring = 'my string'

print(len(mylist))
print(len(mystring))

class movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu.')
    
    def __str__(self) -> str:
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('Film silindi')

m = movie('Film adı', 'Yönetmen', 120)

#print(mylist) #[1, 2, 3]
#print(m)

#print(m.duration) #120 == print(len(m))

del m #m objesini siler

print(m) #Film silindi


**********************************************************************************


#Question class
class question:
    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self,answer):
        return self.answer == answer


#print(q1.checkanswer('Python')) - True
#print(q2.checkanswer('C#')) - False


#Quiz  class
class quiz:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.score = 0
        self.questionindex = 0
        
    def getquestion(self):
        return quiz.questions[self.questionindex]

    def displayquestion(self):
        question = self.getquestion()
        print(f'Soru {self.questionindex + 1}: {question.text}')

        for q in question.choices:
            print('-> ' + q)

        answer = input('Cavap: ')
        self.guess(answer)
        self.loadquestion()

    def guess(self, answer):
        question = self.getquestion()

        if question.checkanswer(answer):
            self.score += 1
        
        self.questionindex += 1

    
    def loadquestion(self):
        if len(self.questions) == self.questionindex:
            self.showscore()
                    
        else:
            self.displayquestion()


    def showscore(self):
        print('Score: ',self.score)


#Soru - seçenekler - cevap
q1 = question('En iyi programlama dili hangisidir ?',['C#','javascript','java','Python'],'Python')
q2 = question('En iyi popüler dili hangisidir ?',['C#','Python','javascript','java'],'Python')
q3 = question('En çok kazandıran programlama dili hangisidir ?',['Python','javascript','C#','java'],'Python')
questions = [q1, q2, q3]

quiz = quiz(questions)

quiz.displayquestion()


**********************************************************************************
