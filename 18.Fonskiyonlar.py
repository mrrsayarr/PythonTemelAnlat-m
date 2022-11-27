
# def demek o parçanın fonkiyon olduğu anlamına gelir.

# def sayHello(name):
#     print('Hello ' + name)
# sayHello('Çınar') # Hello Çınar çıktısını verir.


def sayHello(name = 'user'):
    return 'Hello ' + name
msg = sayHello('Çınar') # Hello Çınar yazdırır.
print(msg)

def total(num1, num2):
    return num1 + num2 
result = total(10,20)
print(result) # 30 çıktısını verir.

def yasHesapla(dogumyili):
    return 2019 - dogumyili
agecinar = yasHesapla(2015)
ageada   = yasHesapla(2010)
print(agecinar, ageada) # 4 9 sonçlarını verir.

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
emeklilignekadarkaldı(1983, 'Ali') # Emekliliğinize 29 yıl kaldı
emeklilignekadarkaldı(1950, 'Ali') # Zaten emekli oldunuz.

print(help(emeklilignekadarkaldı)) 
    #DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    #INPUT: Doğum yılı
    #OUTPUT: Hesaplanan yıl bilgisi

list = [1,2,3]
print(help(list.append)) #Ekleme yapılabileceğini söylüyor.

