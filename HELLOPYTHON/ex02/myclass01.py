class Animal:
    def __init__(self):
        self.age = 1
    def getOld(self):
        self.age+=1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.power_lang = 1
    
    def learn_lang(self):
        self.power_lang += 1
    
    def gawe(self,power):
        self.power_lang += power
        
        
if __name__=='__main__':
    hum = Human()
    print(hum.age)
    print(hum.power_lang)
    hum.getOld()
    hum.learn_lang()
    hum.gawe(5)
    print(hum.age)
    print(hum.power_lang)
    
    ani = Animal()
    print(ani.age)
    ani.getOld()
    print(ani.age)