class Car(object):
 def __init__(self,model,color,company,speed_limit):
    self.color=color
    self.company=company
    self.model=model
    self.speed_limit=speed_limit
 def start(self):
        print("started")
 def stop(self):
        print("stop")
 def accelarate(self):
        print("accelarating")
 def gear(self,gear_type):
        print("changing gear ")

audi = Car("A6", "red", "audi", 80)
print(audi.start())