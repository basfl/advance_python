from pickle_util import Info
from pickle_util import dump_record
if __name__=="__main__":
    items=["a","b","c"]
    info=Info(1,"babak","good",items)
    print(info)
    dump_record(info)