import os
#Testando sequencia lógica e atribuição de variavéis
"""
Este código lê dois números do tipo float representando base e 
altura do e calcula a área do triangulo
"""
resposta="sim"
while resposta=="sim":
    #Entradas
    os.system("cls") #comando para limpar a tela
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    #Processamento
    area = base * altura / 2
    #Saídas
    print(f"A area do triangulo é {area}")
    resposta = input("\nDeseja continuar? (sim/não): ")