

username = 'memo'
password = '1234'

isLoggedin = username=='memoo' and password=='1234'#Yanlış yazdırdık


if isLoggedin:
    print('Şifre Doğru hoşgeldin.') #Hatalı bilgiler girilince burayı atlar.
else:
    print('Bilgileriniz yanlış') #Hatalı bilgiler olduğu için burayı basar.

#************************************************

if (username=='memo') and (password=='1234'): #Kullanıcı adı ve şifre dpğru ise print içindeki ifadeyi basar.
    print('Şifre Doğru hoşgeldin.')

#Eğer kullanıcı Hangisinin doğru olmadığını öğrenmek isterse  
if (username=='memo'):
    if (password =='1234'):
        print('Şifre ve Kullanıcı adı doğru.') #Kullanıcı adı ve Parola doğru ise bu bloğu yazdırır.
    else:
        print('Parolanız yanlış.') #Parola eğer yanlış olursa bir  if 'password' bloğuna geçer ve else bloğu çalışır. 











