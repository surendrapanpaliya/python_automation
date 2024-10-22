
class CarApp:
    '''Car Application For Customer'''

    def info(self,cname):
        '''Car Information Method'''
        self.cname = cname # object / instance variable
        print("It's Audi Car",cname)


AudiCar = CarApp()
#print(AudiCar.__doc__)
AudiCar.info("Audi Car")
print(AudiCar.cname)
