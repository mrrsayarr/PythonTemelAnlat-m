
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



























