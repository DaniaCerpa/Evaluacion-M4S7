#Creación de nueva clase de error

class RangoSalarioError(Exception):
 def __init__(self, salario, salario_maximo = 2000, salario_minimo = 1000):
    self.salario = salario
    self.mensaje = f"Salario no esta definido en el rango ({salario_minimo} a {salario_maximo})"
    self.salario_maximo = salario_maximo
    self.salario_minimo =salario_minimo
    super().__init__(f"{self.salario} -> {self.mensaje}")


#Se define una nueva función
def Rango_salario():

    salario_minimo = 1000
    salario_maximo = 2000
    
    """ Esta función busca conseguir establer si el salario ingresado se encuntra dentro de un determinado rango.  
        De lo contrario retorna un error del tipo RangoSalarioError.
    """
    
    try:
        salario = input("Ingrese el salario: ")
        salario = int(salario)
            
        if salario < salario_minimo or salario > salario_maximo:
            raise RangoSalarioError(salario)
            
        else:
            print("Salario se encuentra dentro del rango")
            return salario 
            
            
    except ValueError:
            print("El dato ingresado es incorrecto. \n Ingresa un número valido")


#Se ejecuta la función para mostrar funcionalidad    
Rango_salario()

