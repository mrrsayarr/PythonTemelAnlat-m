
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#     not aralığına karşılık gelen not bilgisini yazdırınız.
#     0 - 24 => 0
#     25-44 => 1
#     45-54 => 2
#     55-69 => 3
#     70-84 => 4
#     3 85-100 => 5
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

