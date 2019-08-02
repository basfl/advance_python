
from util import insert
from util import read_all
from util import delete
from util import insert
from util import read_one
from util import update


if __name__=="__main__":
    insert("user2","user2***")
    read_all()
    read_one("user2")
    update("user2","password","user2!!!")
    read_one("user2")
    delete("user2")




    
