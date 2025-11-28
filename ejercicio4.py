class Suma:
    def __init__(self, lista):
        self.lista = lista
        self.suma = 0
        self.resultado = self.sumar(lista)

    def sumar(self, lista):
        for i in lista:
           self.suma += i
        return self.suma


lista = [1,2,3,4,5,6,7,8,9]
print(Suma(lista))
resultado = Suma(lista)
print(resultado.resultado)