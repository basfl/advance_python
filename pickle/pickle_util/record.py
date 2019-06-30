class Info:
    def __init__(self, id, name, health, item):
        self.id = id
        self.name = name
        self.health = health
        self.item = item

    def __str__(self):

        return "my id :"+str(self.id)+" name: "+self.name+" health: "+self.health+" item: "+str(self.item)
