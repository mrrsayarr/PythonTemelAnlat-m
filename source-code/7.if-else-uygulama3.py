
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayinız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#      ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız      
#      *** datetime modülünü kullanmanız gerekiyor.
#     (simdi) - (2018/8/1) => gün
import datetime #Modül Kullanma

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
# print(tarih[0]) #2019
# print(tarih[1]) #8
# print(tarih[2]) #9 oalrak yazdırır.

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now() #datetime.now() modülü kodun derlendiği anın saat ve tarihini yazdırır.
fark = simdi - trafigecikis #Aradan geçen zamanın ne kadar olduğunu hesaplamak için farkı alındı.
days = fark.days

if days <= 365:
    print('1.Servis Aralığı ')
elif days > 365 and days <= 365*2:
    print('2.Servis Aralığı ')
elif days > 365*2 and days <= 365*3:
    print('3.Servis Aralığı')
else: 
    print('Hatalı süre') #Eğer girilen süre üzerinden 365*3 gün geçerse bunu yazar.































