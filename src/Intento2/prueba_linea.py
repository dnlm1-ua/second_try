class Linea:
    #Aunque el enunciado pone el orden precio antes de descripcion cambio el orden para adecuarme a anyadirLinea
    def __init__(self, cantidad: int = 0, descripcion: str ='', precio: float = 0.0):
        """ Inicialización de elementos en el constructor  """
        if isinstance(cantidad, int):
            self.cantidad = cantidad
        else:
            raise ValueError("La cantidad debe de ser un entero")
        
        if isinstance(precio, (float,int)):
            self.precio = precio
        else:
            raise ValueError("El precio debe de ser un valor real")
        
        if isinstance(descripcion, str):
            self.descripcion = descripcion
        else:
            raise ValueError("La descripcion se introduce como cadena")
        
    
    #Setters
    def setCantidad(self,cantidad)->int:
        if isinstance(cantidad, int):
            self.cantidad = cantidad
        else:
            raise ValueError("La cantidad debe de ser un entero")

    def setPrecio(self, precio)->float:
         if isinstance(precio, float):
            self.precio = precio
         else:
            raise ValueError("El precio debe de ser un valor entero")
    
    def setDescripcion(self, descripcion):
        if isinstance(descripcion, str):
            self.descripcion = descripcion
        else:
            raise ValueError("La descripcion se introduce como cadena")

    #Getters
    def getCantidad(self)->int:
        return self.cantidad

    def getPrecio(self)->float:
        return self.precio

    def getDescripcion(self)->str:
        return self.descripcion

    def getSubtotal(self)->float:
        return self.cantidad*self.precio
    
    
