# #Identify Operator: is
# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x==y) #True
# print(x==z) #True

# print(x is y) #True değer döner
# print(x is z) #False değer döner  çünkü değerlere bakmaz x ve y nin kendisine bakar.

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















