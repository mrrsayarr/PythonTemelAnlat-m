

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

print(f'c1 : alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}') # c1 : alan = 3.14 çevre = 6.28
print(f'c2 : alan = {c2.alanHesapla()} çevre = {c2.cevreHesapla()}') # c2 : alan = 78.5 çevre = 31.400000000000002