inventario1 = "Espada"
inventario2 = "Poção de cura"
inventario3 = "Escudo"

heroi = input("Qual o nome do seu herói? ")
nivel = int(input("Qual o nível do herói? "))
magia = bool(input("O herói possui Magias?(True/False) "))
vid = int(input("Quantos pontos de vida possui? "))
vid *= 2
Def = int(input("Quanto de armadura o herói possui? "))
print(f"O heroi se chama {heroi}, ele está no nível {nivel} e seus feitos de magia são {magia}")
print(f"O jogador {heroi} possui {vid} pontos de vida.")

print(f"O herói {heroi} acaba de entrar na guilda!")

cidade = input("Viajante, qual o nome da cidade que você está buscando? ")
print(f"Essa cidade... {cidade}, é conhecida por sua população arteira, tome cuidado.")

print(f"Inventário: \n {inventario1}; \n {inventario2}; \n {inventario3}")
print(f"----------\n|Menu    |\n----------")

golpe = int(input("O herói acaba de ser atacado, quanto de dano o ataque causa? "))
DF = Def - golpe
vid -= DF
print(f"A vida atual do jogador é de {vid}")
sal = str(input("Deseja salvar o seu progresso?(S/N) "))

print(f"A tecla teclada foi {sal}")
