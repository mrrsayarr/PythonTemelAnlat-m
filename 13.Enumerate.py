
# index = 0
# greeting = 'Hellothere'

# for letter in greeting:
#     print(f'index: {index} letter: {greeting[index]}') # Indexleri yazdırır.
#     index += 1
# print("\n")
# for index,letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter}') # Indexleri yazdırır. Yukardaki örneğin benzeri.
#     #index: 0 letter: H
#     #index: 1 letter: e
#     #index: 2 letter: l ... gibi yazdırır.
# print("\n")
# for item in enumerate(greeting):
#     print(item)
#     #(0, 'H')
#     #(1, 'e')
#     #(2, 'l') ... gibi yazdırır.
# print("\n")
# for index, item in enumerate(greeting):
#     print(f'index: {index} letter: {item}')

print("\n")
# zip metodu
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
#Liste sayısı arttırılabilir. (Benzer şekilde)
print(list(zip(list1,list2))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] olarak yazar.
print("\n")
for item in zip(list1, list2):
    print(item)
    # (1, 'a')
    # (2, 'b')... olarak çıktı verir.

print("\n")
for a,b in zip(list1, list2):
    print(a,b)
    # 1 a
    # 2 b
    # 3 c
    # 4 d... olaak çıktı verir.



