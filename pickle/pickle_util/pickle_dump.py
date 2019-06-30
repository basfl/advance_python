from pickle_util.record import Info
import pickle

def dump_record(info):
    with open("save1.pkl","wb") as output:
        pickle.dump(info,output,pickle.HIGHEST_PROTOCOL)
    print("_____reverse____")
    newObj=None
    with open("save1.pkl","rb") as input:
        newObj=pickle.load(input)
    print(newObj)


if __name__=="__main__":
    items=["a","b","c"]
    info=Info(1,"babak","good",items)
    print(info)
    dump_record(info)