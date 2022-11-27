'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
    
'''
sayi = float(input('sayı: '))
result = (sayi > 0) and (sayi<=100)

if result:
    print(f'Sayı 0-100 arasındadır.')
else:
    print('Sayı 0-100 arasında değildir.')


