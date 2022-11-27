
# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#   durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve eğitim durumu
#   lise ya da üniversite olmalıdır. 
from unicodedata import name


isim = input('isminiz: ')
yas = int(input('Yaşınız: '))
egitim = input('Eğitim: ')

# if (yas > 18) and (egitim == 'lise' or egitim =='üniversite'):
#     print('Ehliyet alabilirsiniz.') #Yaş 18 den büyük ve eğitimin lise veya üniversite olması gerekmektedir.
# else:
#     print('Ehliyet alamazsınız.')

#Ehliyetin neyden dolayı alınamadığını öğrenmek için
if (yas > 18):
     if (egitim == 'lise' or egitim =='üniversite'):
        print(f'{isim} Ehliyeti alabilirsin.') #Yaş 18 den büyük ve eğitimin lise veya üniversite olması gerekmektedir.
     else: 
         print(f'{isim} Eğitim durumunuzdan dolayı ehliyet alamazsın.')
else:   
     print(f'{isim} yaşınızdan dolayı ehliyet alamazsınız.')
 












