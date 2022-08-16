#calculadora con Clases


class Calculadora:
    def __init_(self):
        self.numero1= None
        self.numero2= None


    def sumar(self,numero1,numero2):
        resultado =numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")


    def restar(self,numero1,numero2):
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")

    def multiplicar(self,numero1,numero2):
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")


    def dividir(self,numero1,numero2):
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado} ")




calculadora = Calculadora()


while True:
    print("""\tCalculadora
1.Sumar
2.Restar
3.Multiplicar
4.Dividir
5.salir""")
    opcion = int(input("Digite una opcion: "))
    print()
    if opcion == 1:
        numero1 = int(input("Digite el primer numero: "))
        numero2 = int(input("Digite el segundo numero: "))
        calculadora.sumar(numero1,numero2)
    elif opcion ==2:
        numero1 = int(input("Digite el primer numero: "))
        numero2 = int(input("Digite el segundo numero: "))
        calculadora.restar(numero1,numero2)
    elif opcion==3:
        numero1 = int(input("Digite el primer numero: "))
        numero2 = int(input("Digite el segundo numero: "))
        calculadora.multiplicar(numero1,numero2)
    elif opcion==4:
        numero1 = int(input("Digite el primer numero: "))
        numero2 = int(input("Digite el segundo numero: "))
        calculadora.dividir(numero1,numero2)
    elif opcion==5:
        break
    else:
        print("Se equivico de opcion")
        print()

        

