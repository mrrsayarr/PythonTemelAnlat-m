

sayi = input("Bir ifade giriniz: ")

def palindrom(sayi): # input ile alınan ifadeyi parametre olarak çağırıyoruz
        return sayi[::-1] # Girilen ifade ters döner


ters = palindrom(sayi) # Girilen sayıyı fonkisyon yardımıyla ters çeviriyoruz

if sayi == ters: # Eğer palindrom ise burası çalışır
        print("Palindrom")
else: # Eğer palindrom değilse burası çalışır
        print("Not Palindrom")

