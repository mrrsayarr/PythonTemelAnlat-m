
# Inheritance (Kalıtım): Miras  ALma
 
# Person => name, lastname, age, eat(), run(), drink()
# Student, Teacher da olmasını isteriz
# Bu yzüden Studen(Person), Teacher(Person) ile Person Sınıfını miras alırız.

#Ya da 

# Animal => Dog(Animal), Cat(Animal) gibi ...

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person created')

    def who_am_i(self):
        print('I am a Person :(')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self,fname,lname)
        self.studentnumber = number
        print('Student created')

    #override
    def who_am_i(self): # Yukarıda ki fonksiyonu ezmek (override etmek) için kullanıldı
        print('I am a Student :)') # Override edilen fonka yazılan yeni Metin

    def sayhello(self):
        print('Helllo I am a STUDENT')
        
class Teacher(Person):
    def __init__(self,fname,lname, branch):
        super().__init__(fname,lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} TEACHER')
        

t1 = Teacher('Serkan','Arı','SOFTWARE')
p1 = Person('Mehmet', 'Ata')
s1 = Student('Ali', 'Bşaran','12356') # number sadece Student'a özel olduğu için sadece burda yazılabilir
#Person created
#Student created - Miras  alıyor

print(p1.firstname + ' ' + p1.lastname) # Mehmet Ata
print(s1.firstname + ' ' + s1.lastname + ' ' + s1.studentnumber) #  Ali Bşaran 12356

t1.who_am_i() # I am a SOFTWARE TEACHER
p1.who_am_i() # I am a Person
s1.who_am_i() # I am a Person

p1.eat() # I am eating
s1.eat() # I am eating

s1.sayhello() # Hello I am a STUDENT "Sadece Student'a ait bir yapıdır"




