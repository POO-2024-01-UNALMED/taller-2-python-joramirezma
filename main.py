class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        colores=("rojo","verde","amarillo","negro","blanco")
        if color in colores:
            self.color=color

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        Auto.cantidadCreados=cantidadCreados
    
    def cantidadAsientos():
        cantidad=0
        for i in self.asientos:
            if self.asientos[i] != None:
                cantidad+=1
        return cantidad
    
    def verificarIntegridad():
        verificador="si"
        if (self.motor.registro==self.registro):
            for j in self.asientos:
                if self.asientos[j].registro != self.registro:
                    verificador="no"
        else:
            verificador="no"

        if verificador=="si":
            return "Auto original"
        else:
            return "Las piezas no son originales"


class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(registro):
        self.registro=registro

    def asignarTipo(tipo):
        tipos=("gasolina","electrico")
        if tipo in tipos:
            self.tipo=tipo

