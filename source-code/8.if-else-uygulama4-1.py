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





























