
AliHesap = {
    'ad': 'Ali Pala',
    'hesapNo': '11111111',
    'bakiye': 3000,
    'ekHesap': 2000
}
AyseHesap = {
    'ad': 'Ayse Pala',
    'hesapNo': '22222222',
    'bakiye': 200,
    'ekHesap': 1000
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar :
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesaptan para çekilsin mi ? (e/h)')
            
            if ekHesapKullanimi == 'e':
                bakiye = hesap['bakiye']
                ekhesapkulllanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapkulllanilacakmiktar
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        
        else:
            print('Üzgünüm bakiyeniz yetersiz.')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır. ")



paraCek(AliHesap, 3000)
bakiyeSorgula(AliHesap)

print(' *****************')

paraCek(AliHesap, 2000)





















