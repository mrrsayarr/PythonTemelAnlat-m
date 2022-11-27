'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız.

'''
email = 'email@gmail.com'
password = 'abc123'

girilenemail = input('Email: ')
girilenpassword = input('Password: ') 
                              
result = (girilenemail == email) and (girilenpassword == password)

if (girilenemail == email):
    if (girilenpassword == password):
        print(f'Uygulamaya giriş başarılı.')
    else:
        print('Yanlış Parola girdiniz.')
else:
    print(f'Email bilgisi yanlış')



















