#Peça três informaões ao usuário, : Nome, Nivél(int) e se tem magia(bool). Depois, use o print() para mostrar tudo formatado em uma única linha.

heroi = input("Qual o nome do seu herói? ")
nivel = int(input("Qual o nível do herói? "))
magia = bool(input("O herói possui Magias?(True/False) "))


if magia == True:
    
    print(f"----------------\n\
|Ficha do herói:|\n\
|Herói: {heroi} |\n\
|nivel:{nivel}  |\n\
|magias:Sim     |\n\
---------------")
    
elif magia == False:
    print(f"----------------\n\
|Ficha do herói:|\n\
|Herói: {heroi} |\n\
|nivel:{nivel}  |\n\
|magias:Não     |\n\
----------------")

