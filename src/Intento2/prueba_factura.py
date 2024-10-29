from .prueba_linea import Linea

class Factura:
    IVA = 21
    sigId = 1  # Variable de clase para el id de la factura

    def __init__(self, cliente, fecha):
        self.id = Factura.getSigId()  # Obtener e incrementar el ID
        self.cliente = cliente
        self.fecha = fecha
        self.lineas = []

    @staticmethod
    def getSigId():
        # Obtener el ID actual y luego incrementarlo
        id_actual = Factura.sigId
        Factura.sigId += 1
        return id_actual

    def anyadirLinea(self, cant, desc, prec):
        # Crear una nueva línea de producto
        linea = Linea(cant, desc, prec)
        self.lineas.append(linea)

    def __str__(self):
        # Formatear la salida de la factura
        resultado = f"Factura nº: {self.id}\nFecha: {self.fecha}\n"
        resultado += "Datos del cliente\n-----------------\n"
        resultado += f"Nombre: {self.cliente.getNombre()}\n"
        resultado += f"Dirección: {self.cliente.getDireccion()}\n"
        resultado += f"Teléfono: {self.cliente.getTelefono()}\n"
        resultado += "Detalle de la factura\n---------------------\n"
        resultado += "Línea;Producto;Cantidad;Precio ud.;Precio total\n"

        subtotal = 0
        for idx, linea in enumerate(self.lineas, 1):
            subtotal_linea = linea.getSubtotal()
            resultado += f"{idx};{linea.getDescripcion()};{linea.getCantidad()};{linea.getPrecio()};{subtotal_linea}\n"
            subtotal += subtotal_linea

        iva = subtotal * Factura.IVA / 100
        total = subtotal + iva
        resultado += f"Subtotal: {subtotal:.2f} €\n"
        resultado += f"IVA ({Factura.IVA}%): {iva:.4f} €\n"
        resultado += f"TOTAL: {total:.4f} €\n"
        return resultado
