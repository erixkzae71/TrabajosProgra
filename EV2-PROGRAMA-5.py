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

punto1 = Punto(10, 2)
punto1.imprimir()
punto1.imprimir_cuadrante()
