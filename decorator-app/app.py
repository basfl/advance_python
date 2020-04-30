from util import someting
from util import somethingargs


@someting
def my_func():
    print("inside the function")


@somethingargs(2)
def add(n1, n2):
    return n1+n2
class A:
    def __str__(self):
        return "Object A"
    def __repr__(self):
        return "a=A()"
    @staticmethod
    @somethingargs(2)
    def add1(n1,n2):
        return n1+n2

if __name__ == "__main__":
    print("****")
    my_func()
    print(add(2, 3))
    a=A()
    print("*******\n")
    print(f"repre for object is {a.__repr__()}")
    print("*******\n")
    print(f"str for object is {a}")
    print(a.add1(4,4))
