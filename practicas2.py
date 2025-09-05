# Clases y objetos.

class carro:

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


    def informacion(self):
        print(f"El vehiculo que elegiste es un {self.marca}, modelo {self.modelo}, año {self.año} ")
    

    
carro1 = carro("Ford","Fiesta","2005")
carro2 = carro("Toyota","Hilux","2024")

carro1.informacion()
carro2.informacion()














        
