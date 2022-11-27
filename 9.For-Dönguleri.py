

numbers = [1,2,3,4,5]

#Eğer for döngüsü olmasaydı bunların hepsini elle yazmak zorunda kalacaktık.
# print(numbers[0]) #1
# print(numbers[1]) #2
# print(numbers[2]) #3
# print(numbers[3]) #4
# print(numbers[4]) #5 çıktılarını verirler 
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

