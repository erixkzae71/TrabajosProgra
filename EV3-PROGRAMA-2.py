class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("Coordenada del punto")
        print("(", self.x, ",", self.y, ")")

    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")

# Bloque principal
punto1 = Punto(100, 2)
punto1.imprimir()
punto1.imprimir_cuadrante()
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
for e in Entradas:
 print(f'{e[0]}|{e[1]}|{e[2]}')
Datos=[]