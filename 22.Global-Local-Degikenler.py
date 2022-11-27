
name = 'Ali'

def changename(newname):
    name = newname
    print(name) # Memo

changename('Memo')
print(name) # Ali

#############################

name = 'Global String'
def greeting():
    # name = 'Ali' -- Yorum satırı kaldırılırsa hello Ali yazar.

    def hello():
        print('Hello' + name)
    
    hello()
greeting()
# hello Global String i yazdırır.

#############################

x = 50
def test():
    global x
    
    print(f'x: {x}')

    x = 100
    print(f'Changed x to {x}')
test()
print(x)
    #x: 50 (global x yazılırsa)
    #Changed x to 100 (global x yazılırsa)
    #100 (global x yazılırsa)

#############################
x = 50
def test(x):
    print(f'x: {x}')

    x = 100
    print(f'Changed x to {x}')
test(x)
print(x)
    # x: 50
    # Changed x to 100
    # 50