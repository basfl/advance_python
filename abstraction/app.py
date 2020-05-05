from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Horse(Animal):
    def move(self):
        print(f"horses can run !!")

class Snake(Animal):
    def move(self):
        print(f"snake can crawl !!")

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    # can return any expression
    def __repr__(self):
         return '{name:'+self.name+', age:'+str(self.age)+ '}'
    # Must return string
    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

if __name__=="__main__":
    h=Horse()
    h.move()
    s=Snake()
    s.move()
# ---------------- 
    p=Person("person",12)
    # __str__() example
    print(p)
    print(p.__str__())
    s = str(p)
    print(s)
    print("\n--------------")
    # __repr__() example
    print(p.__repr__())
    print(f'${type(p.__repr__())}')
    print(f'{repr(p)}')


