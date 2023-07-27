class Galleta():
    chocolate = False 
    
    def __init__(self):
       print("Se acaba de crear una galleta.")
       
    def chocolatear(self):
        print("Vamos a chocolatear la galleta")
        self.chocolate = True
    def tiene_chocolate(self):
        if (self.chocolate == True):
            print("Soy una galleta chocolateada!!!\n (●'◡'●) ")
        
        else:
            print("Soy una galleta sin chocolate...\n ಥ_ಥ")
        
print("GALLETA 1")
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()
print("GALLETA 2")
g2 = Galleta()
g2.tiene_chocolate()            
