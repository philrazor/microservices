class Person():
    name = 'phil'
    age  = 22

    def return_defaults(self):
        return (self.name , self.age)


p1 = Person()

defaults = p1.return_defaults()

for item in defaults:
    print(item)

for i in range(len(defaults)):
    print(defaults[i] , i)

class Check_defaults():
    def __init__(self , defaults) -> None:
        self.defaults = defaults 
    