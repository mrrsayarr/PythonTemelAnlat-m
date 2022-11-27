

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

    # instance methods
    def intro(self):
        print('Hello there. I am ' + self.name) # Hello there. I am ali
  
    # instance methods
    def calculateAge(self):
        return 2019 - self.year

# Object (instance)
p1 = Person(name = 'ali', year = 1990) #name : ali , year: 1990
p2 = Person('ayse', year = 1992) #name : ayse , year: 1992

p1.intro() # Hello there. I am ali
p2.intro() # Hello there. I am ayse

print(f'Adım: {p1.name} ve Yaşım: {p1.calculateAge()}') # Adım: ali ve Yaşım: 29 
print(f'Adım: {p2.name} ve Yaşım: {p2.calculateAge()}') # Adım: ayse ve Yaşım: 27