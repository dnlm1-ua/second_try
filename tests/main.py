import Intento2 as mp

def test_cliente():
    print("Prueba de Cliente:")
    cliente = mp.Cliente("Agapito Piedralisa", "c/ Río Seco, 2", "123456789")
    
    if cliente.getNombre() == "Agapito Piedralisa":
        print(" - getNombre: Correcto")
    else:
        print(" - getNombre: Error")

    if cliente.getDireccion() == "c/ Río Seco, 2":
        print(" - getDireccion: Correcto")
    else:
        print(" - getDireccion: Error")

    if cliente.getTelefono() == "123456789":
        print(" - getTelefono: Correcto")
    else:
        print(" - getTelefono: Error")

def test_linea():
    print("\nPrueba de Linea:")
    linea = mp.Linea(2, "Ratón USB", 8.43)
    
    if linea.getCantidad() == 2:
        print(" - getCantidad: Correcto")
    else:
        print(" - getCantidad: Error")
    
    if linea.getDescripcion() == "Ratón USB":
        print(" - getDescripcion: Correcto")
    else:
        print(" - getDescripcion: Error")

    if abs(linea.getPrecio() - 8.43) < 0.01:
        print(" - getPrecio: Correcto")
    else:
        print(" - getPrecio: Error")

    if abs(linea.getSubtotal() - 16.86) < 0.01:
        print(" - getSubtotal: Correcto")
    else:
        print(" - getSubtotal: Error")

def test_factura():
    print("\nPrueba de Factura:")
    cliente = mp.Cliente("Agapito Piedralisa", "c/ Río Seco, 2", "123456789")
    factura = mp.Factura(cliente, "18/04/2011")
    
    if factura.cliente.getNombre() == "Agapito Piedralisa":
        print(" - cliente.getNombre: Correcto")
    else:
        print(" - cliente.getNombre: Error")

    factura.anyadirLinea(1, "Ratón USB", 8.43)
    factura.anyadirLinea(2, "Memoria RAM", 21.15)
    
    if len(factura.lineas) == 2:
        print(" - anyadirLinea: Correcto")
    else:
        print(" - anyadirLinea: Error")

    print("\nResultado de factura:\n")
    print(factura)

# Ejecutar pruebas manualmente
if __name__ == "__main__":
    test_cliente()
    test_linea()
    test_factura()
