class house:
    def __init__(self, door,window, room):
        self.door=str(door)
        self.window=str(window)
        self.room=str(room)
        print("the house has  "+self.door+ ","+self.window+" , "+self.room)


class chouse(house):
    def __init__(self, door, window, room,houseno):
        super().__init__(door, window, room)
        self.houseno=houseno
        print("the house has  "+self.door+ ","+self.window+" , "+self.room,self.houseno)

childhouse = chouse(6,7,8,"D9")
# basehour=house(3,2,1,"D9")