import random

tiranoVida = 1000
vid = 100

espada = 0
espada1 = True
armadura = True
tirano = True
print(f"O herói está em uma jornada para derrubar o Rei Tirano. ")
while tirano == True:
    
    x = 0
    y = 0
    
    print("|-------------------------------------------------------|")
    print("|Mapa:\n x = 6, e y = 0: Caverna Escondida.             |")
    print("|x = 0, y = 0: Acapamento rebelde.                      |")
    print("|x = -2, e y = 5: Castelo do Tirano.                    |")
    print("|-------------------------------------------------------|")
    
    x += int(input("Digite a coordenada para x: "))
    y += int(input("Digite a coordenada para y: "))
    print(f"O heroi se moveu para({x},{y})")
    
    if x == 6 and y == 0 and espada1 == True:
        print("O heroi encontrou a espada sagrada, agora ele capaz de causar dano ao Tirano.")
        espada += 100
        espada1 = False
        
    if x == -2 and y == 5 and armadura == True:
        print("O herói entrou no acampamento rebelde e recebeu uma armadura!")
        vid += 900
        armadura = False
        
    if x == -2 and y == 5 and tirano == True:
        while tiranoVida > 0:
            ataque = random (1,2)

            print("!!! A batalha final está para começar !!!")
            
