#Classifica fase da vida
"""
Este código lê uma idade e informa a fase da vida

"Bebê", quando a idade for menor ou igual a 2 
"Criançã", quando a idade for menor ou igual a 10
"Pré-adolescente", menor que 15
"Adolescente", menor que 18
"Jovem", menor ou igual a 30
"Adulto", menor que 60
"Véio", maior ou igual a 60
"""

idade= int(input("Informe a sua idade: "))
if idade<=2:
    print("Bebê")
elif idade<=10:
    print("Criança")
elif idade<15:
    print("Pré-adolescente")
elif idade<18:
    print("Adolescente")
elif idade<=30:
    print("Jovem")
elif idade<60:
    print("Adulto")
else:
    print("Véio")
    print(f"Você esta na fase: {idade}")
    



    