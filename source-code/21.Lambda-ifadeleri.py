#Map-Filter

import numbers


def square(num): return num ** 2

numbers1 = [1, 3, 5, 7, 4, 6]

result = list(map(square, numbers1))
# map metodu bellektki adresi verir. Fakat list ile yazdırırsak bize numebrs listesini çağırır.
for item in map(square, numbers1):
    print(item)

#Veya başka bir kullanım yolu da

numbers2 = [2, 4, 6, 8]
result = list(map(lambda num: num ** 2, numbers2))
print(result) #[4, 16, 36, 64] olarak çıktı verecektir.

#*****************************************************
numbers1 = [1, 3, 5, 7, 4, 6]

def check_even(num): return num % 2 == 0
result = list(filter(check_even, numbers1))
print(result) # [4, 6] olarak yazar.

#Veya

result = list(filter(lambda num: num%2==0, numbers1))
print(result)

#Ya da

check_even = lambda num: num%2==0
result = check_even(numbers[2])#Sayı tek olduğu için False bilgisini döner.
print(result)






