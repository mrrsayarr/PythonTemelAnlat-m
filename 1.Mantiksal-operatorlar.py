
x = 6
result = 5 < x < 10 #True değeri döner.
#ve
result = x > 5 and x < 10 #True
#veya
result = x > 5 or x % 2 == 0 #True, and olursa False olur.
#not
result = not(x > 5) #False 
# x, 5-10 arasında olan bir çift sayı mı?
result = x > 5 and x < 10 and x % 2 == 0 #True döner
result = x < 5 and x < 10 and x % 2 == 0 #False döner

print(result)






