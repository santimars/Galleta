class Galletas():
    chocolate = False
    sabor = "Dulce" # estos son atributos globales  todas la variables que tengan la clase Galleta() todos tendran estos atributos por defecto
    
g = Galletas()
print(g.chocolate)

#🍪 estamos haciendo galletas
# estamos cambiado su atributo pordefecto todo lo que yo cree en una variavle va a hacer True

''                                                       '''metodo init() - CONSTRUCTOR'''
'''
Se llama automaticamente al crear una distancia de clase

'''

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
            print("Soy una galleta sin chocolate...\n (ಥ _ಥ)")
        
print("GALLETA 1")
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

print("\nGALLETA 2")
g2 = Galleta()
g2.tiene_chocolate()            

'''                                                      Parametros ene el Int(argumentos al instalar)                                                     '''


# recomendacion sar siempre el constructor 
# escribirlo desde el principio
'''


'''
class Galleta():

 def __init__(self, sabor = None, forma = None, chocolate = None):
     self.sabor = sabor
     self.forma = forma
     self.chocolate = chocolate

     if self.sabor is not None and self.forma is not None and self.chocolate is not None:
       print("Se acaba de crear una Galleta {}, {} y {}".format(self.sabor,self.forma,self.chocolate))
     else:
       print("Se acaba de crear una Galleta, pero...")
       if self.sabor is None:
           print("> El sabor no se ha definido")
       if self.forma is None:
           print("> La forma no se ha definido")
       if self.chocolate is None:
           print("> El chocolate no se ha definido")

 def chocolatear(self):
  self.chocolate = True

 def tiene_chocolate(self):
  if (self.chocolate):
   print("Soy una galleta chocolateada :D")
  else:
   print("Soy una Galleta sin Chocolate :(")
