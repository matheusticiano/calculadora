#Alunos Matheus Ticiano e Higor Matheus

while True :
    operação = input("Qual operação será realizada ? (+ , - , / , * , raiz , ! ) ")
    try :
        if (operação == "raiz" ) or (operação == "!"):
            num1 = float(input(" Qual o numero :"))
            break

        elif (operação == "+") or (operação == "/") or (operação == "*")  or (operação == "-") :
            num1 = float(input("Primeiro numero :"))
            num2 = float(input("Segundo numero :"))
            break
        else :
            print("Escolha uma operaçâo valida")


    except :
            print("Digite valores validos !")

def soma():
    print(f'o resultado da soma é: {num1 + num2} ')


def subtração():
    print(f'o resultado da subtração é: {num1 - num2} ')


def multiplicação():
    print(f'o resultado da multiplicação é: {num1 * num2} ')


def divisão():
    print(f'o resultado da divisão é: {num1 / num2} ')


def raiz():
    print(f'A raiz de {num1} é: {num1 ** 0.5} ')


def fatorial():
    resultado = 1
    count = 1

    while count <= num1:
        resultado *= count
        count += 1

    print(f'O resultado da fatoração é {resultado}')


if operação == "+":
    soma()
elif operação == "-":
    subtração()
elif operação == "*":
    multiplicação()
elif operação == "/":
    divisão()
elif operação == "raiz":
    raiz()
elif operação == "!":
    fatorial()
else:
    print(" OOPS!!! , Aconteceu algum Erro !")

