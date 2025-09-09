#projeto de calculadora

def soma(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)


def mult(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

print("digite os elementos numericos e a operação que deseja executar")

while True:

    elemento_num = float(input("elemento numerico: "))
    operacao_num = input("operacao numerico: ")
    elemento_num2 = float(input("segundo elemento numerico: "))

    if operacao_num == "+":
        soma(elemento_num,elemento_num2)
    elif operacao_num == "-":
        sub(elemento_num,elemento_num2)
    elif operacao_num == "*":
        mult(elemento_num,elemento_num2)
    elif operacao_num == "/":
        if elemento_num2 != 0:
            div(elemento_num,elemento_num2)
        else:
            print("erro de divisao por zero.")
            break
    else:
        print("operacao invalida ou numero invalido.")
        break


