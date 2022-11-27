
mylist = [1,2,3]
mystring = 'my string'

print(len(mylist))
print(len(mystring))

class movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu.')
    
    def __str__(self) -> str:
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('Film silindi')

m = movie('Film adı', 'Yönetmen', 120)

# print(mylist) # [1, 2, 3]
# print(m)

#print(m.duration) # 120 == print(len(m))

del m # m objesini siler

print(m) # Film silindi







