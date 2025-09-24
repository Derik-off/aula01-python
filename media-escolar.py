nome = input("Nome do aluno: ")
n1 = float(input("Digite o primeiro bimestre: "))
n2 = float(input("Digite o segundo bimestre: "))
n3 = float(input("Digite o terceiro bimestre: "))
n4 = float(input("Digite o quarto bimestre: "))
n5 = n1 + n2 + n3 + n4
n6 = n5 / 4
if n6>=5:
    print("O aluno", nome, "tirou",n6, "foi aprovado")
elif n6<5:
    print ("O aluno", nome," tirou ",n6, "foi reprovado")


