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

if __name__=="__main__":
    h=Horse()
    h.move()
    s=Snake()
    s.move()

