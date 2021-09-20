
class Person():
    #class constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def pname(self):
        print('name = ',self.name)

    #create class setters

    #create class getters
    def name(self):
        return self.name()

    def age(self):
        return self.age()


person1 = Person('vasia',25)
print(person1.name, person1.age)
person1.pname()
print('--------------------')
# print(person1.name())
# print(person1.age())



from mutators import P
p1 = P(-42)
p1.set_x(-42)
p2 = P(4711)
print(p1.get_x())

from mutators import Q
p1 = Q(42)
p2 = Q(4711)
print(p1.x)

from mutators import Default
s1 = Default()
print(s1)
