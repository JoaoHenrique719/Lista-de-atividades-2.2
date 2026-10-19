inventario1 = "Espada"
inventario2 = "Poção de cura"
inventario3 = "Escudo"
energia = 100
heroi = input("Qual o nome do seu herói? ")
nivel = int(input("Qual o nível do herói? "))
magia = bool(input("O herói possui Magias?(True/False) "))
vid = int(input("Quantos pontos de vida possui? "))
vid *= 2
escudo = int(input("Quanto de armadura o herói possui? "))
escudo_energia = 100
x = 0
y = 0

print(f"O heroi se chama {heroi}, ele está no nível {nivel} e seus feitos de magia são {magia}")
print(f"O jogador {heroi} possui {vid} pontos de vida.")

print(f"O herói {heroi} acaba de entrar na guilda!")

x += int(input("Digite a cordenada para altura: "))
y += int(input("Digite a coordenada para comprimento: "))
print(f"O heroi se moveu para({x},{y})")

cidade = input("Viajante, qual o nome da cidade que você está buscando? ")
print(f"Essa cidade... {cidade}, é conhecida por sua população arteira, tome cuidado.")

print(f"Inventário: \n {inventario1}; \n {inventario2}; \n {inventario3}")
print(f"----------\n|Menu    |\n----------")

golpe = int(input("O herói acaba de ser atacado, quanto de dano o ataque causa? "))
DF = escudo - golpe
vid -= DF
escudo_energia -= 50
energia -= 20

print(f"O escudo do jogador tem {escudo} de defesa, o golpe atingido causa {DF} de dano, vida atual do jogador é de {vid}")
print(f"A energia está em {energia}%, e o escudo está em {escudo}%")
sal = str(input("Deseja salvar o seu progresso?(S/N) "))

print(f"A tecla teclada foi {sal}")
