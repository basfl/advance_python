def someting(fn):
    def wrapper(*args,**kwargs):
        print("before function")
        result=fn(*args,**kwargs)
        print("after function")
        return result
    return wrapper

def somethingargs(param):
    def outter(fn):
        def wrapper(*args,**kwargs):
            rs=fn(*args,**kwargs)
            final=rs*param
            print(f"final is {final}")
            return final
        return wrapper
    return outter


