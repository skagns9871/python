class Dog:
    def __init__(self):
        self.power_bark = 0
    def teachFromHuman(self):
        self.power_bark +=1
        
class Bird(Dog):
    def __init__(self):
        super().__init__()
        self.power_fly = 0
    

def exercise(self,power):
    self.power_fly += power
        
        
if __name__=='__main__':
    # bird = Bird()
    # print(bird.power_fly)
    # print(bird.power_bark)
    # bird.exercise(5)
    # bird.exercise(6)
    # bird.teachFromHuman()
    # bird.teachFromHuman()
    # bird.teachFromHuman()
    # print(bird.power_bark)
    # print(bird.power_fly)
    print(exercise.power())