import random

tiranoVida = 1000
vid = 100


Espada = False
ouro = 0
aldeia = True
espada1 = True
armadura = True
tirano = False
Tirano = True
print(f"O herói está em uma jornada para derrubar o Rei Tirano. ")
while Tirano == True:
    
    x = 0
    y = 0
    goblin_vida = 250
    
    print("|-------------------------------------------------------|")
    print("|Mapa:                                                  |")
    print("| x = 6, e y = 0: Caverna Escondida.                    |")
    print("|x = -2, y = 5: Acapamento rebelde.                     |")
    print("|x = 9, y = 6: Aldeia de Goblins                        |")
    print("|x = -2, e y = 5: Castelo do Tirano.                    |")
    print("|-------------------------------------------------------|")
    
    x += int(input("Digite a coordenada para x: "))
    y += int(input("Digite a coordenada para y: "))
    print(f"O heroi se moveu para({x},{y})")
    
    if x == 6 and y == 0 and espada1 == True:
        print("O heroi encontrou a espada sagrada, agora ele capaz de causar dano ao Tirano.")
        espada1 = False
        Espada = True
        
    if x == -2 and y == 5 and armadura == True:
        print("O herói entrou no acampamento rebelde e recebeu uma armadura!")
        vid += 900
        armadura = False
        
    if x == 9 and y == 6 and aldeia == True:
        print("O heroi invadiu a aldeia de goblins! Ele vai ser atacado, qual a ação do herói?")
        
        while goblin_vida > 0:
            ataque_goblin = random.randint(100, 200)
            vid -= ataque_goblin
            ac = str(input(f"O goblin te atacou, você está com {vid} pontos de vida, o heroi vai atacar(A), usar uma poção(B) ou irá fugir(C)?" ))
            
            if ac == "A" and espada1 == True:
                ataque_heroi = random.randint(150, 250)
                goblin_vida -= ataque_heroi
                print(f"O herói não se acorvadou e atacou o goblin, o goblin está com {goblin_vida} pontos de vida.")
                
                
                
        
        
        
    if x == -2 and y == 5 and tirano == True:
        while tiranoVida > 0:
            

            print("!!! A batalha final está para começar !!!")
            
