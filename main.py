#1
def mama(*args):
    k=0
    s=0
    for znach in args:
        s=s+int(znach)
        k=k+1
    print(s/k)
mama(1, 2, 3, 4, 5)

#2
b=[]
def ryadki(*args):
    for i in args:
        r=len(i)
        b.append(r)
    for j in b:
        maxi=b[0]
        if int(j)>maxi:
            maxi=int(j)
    print(maxi)
ryadki("abc", "defg", "hijkl", "moidshf;hg")

#3
b=[]
def ryadki(*args):
    for i in args:
        b.append(i)
    print(' '.join(args))
ryadki("abc", "defg", "hijkl", "mnopqrstuvw")

#4
people=[('nikita', 15), ('ludina', 45), ('gleb', 1)]
def create_dict(*args):
    name_age={}
    if args:
        for name, age in args:
            name_age[name]=age
    return name_age
print(create_dict(people))
























class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name, "eating")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed=breed
    def bark(self):
        print(self.name, 'barking')
hotdog=Dog("bobik", 3, 'blablador')
print(hotdog.name)
print(hotdog.age)
print(hotdog.breed)
hotdog.eat()

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'Name {self.name}, age {self.age}'
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id=student_id
    def __str__(self):
        return super().__str__()+f" student_id {self.student_id}"
student1=Student("mama", 21, 777)
with open('info_student.txt', 'w') as file:
    file.write(str(student1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   import random
class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        super().__init__()
        self.apecies=species
        self.name=name
        self.age=age
        self.health=health
        self.hunger=hunger
        self.happines=happines
    def grow(self):
        self.age+=1
        self.health=random.randint(0, 10)
        self.hunger=random.randint(0, 10)
        self.happines=random.randint(0, 10)
    def eat(self):
        if self.hunger >=6:
            self.health += random.randint(0, 5)
            self.happines += random.randint(0, 5)
            self.hunger -= random.randint(5, 7)
        else:
            print(self.name, "hungry")
    def play(self):
        pass #happines

class Zoo:
    def __init__(self):
        super.__init__()
        self.animal=[]
