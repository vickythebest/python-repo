#class
#blueprint/formula/skeleton



#objects

#e.g, human bod : skeleton is a class and people
#e.g vehicle is a class V1, v2,v3
# object will have same properties but value will be different

#class for creating vehicle

class vehicle:
    def __init__(self, color,wheels):
        self.color=color
        self.wheels=wheels

        print("hey , your car color is "+self.color, self.wheels)



#create a class called as "vehicle" it should accept the properties of two field

veh1=vehicle("blue",4)
veh2=vehicle("yellow",3)
#veh1 (color read and wheels 4)
#veh2 (color yello and sheels 3)
#veh3 (color black and wheels 2)