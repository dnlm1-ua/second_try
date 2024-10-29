class Cliente:
    def __init__(self, nombre: str='', direccion: str='', telefono: str=''):
        """ Inicialización de elementos del constructor """
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena")
        
        if isinstance(direccion, str):
            self.direccion = direccion
        else:
            raise ValueError("La direccion debe ser una cadena")
        
        if isinstance(telefono, str):
            self.telefono = telefono
        else:
            raise ValueError("El telefono debe ser una cadena")
    
    #Setters
    def setNombre(self, nombre)->str:
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena")
    
    def setDireccion(self, direccion)->str:
        if isinstance(direccion, str):
            self.direccion = direccion
        else:
            raise ValueError("La direccion debe ser una cadena")
    
    def setTelefono(self, telefono)->str:
        if isinstance(telefono, str):
            self.telefono = telefono
        else:
            raise ValueError("El telefono debe ser una cadena")
    

    #Getters
    def getNombre(self)->str:
        return self.nombre
    
    def getDireccion(self)->str:
        return self.direccion
    
    def getTelefono(self)->str:
        return self.telefono
    
    
        
        
        
        