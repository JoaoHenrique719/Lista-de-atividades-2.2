import random

tiranoVida = 1000
vid = 100

crosta = True
Espada = False
aldeia = True
espada1 = True
armadura = True
ouro = 0
poc_vid = 0
ped_pre = 0

tirano = False
Tirano = True
print(f"O herói está em uma jornada para derrubar o Rei Tirano. ")
while Tirano == True:
    
    x = 0
    y = 0
    goblin_vida = 250
    
    print("|-----------------------------------------------------------|")
    print("|Mapa:------------------------------------------------------|")
    print("|x = 6, y = 0: Caverna Escondida(recebe a espada sagrada).--|")
    print("|x = 2, y = 5: Acapamento rebelde(recebe a armadura).------ |")
    print("|x = 9, y = 6: Aldeia de Goblins(acumular ouro).----------- |")
    print("|x = 3, y = 8: viajante(gastar o ouro).---------------------|")
    print("|x = 7, y = 9: Crosta das Sereias(acumular pedras preciosa).|")
    print("|x = 4, y = 7: Minerador(Gastar pedras preciosas).----------|")
    print("|x = 10, y = 10: Castelo do Tirano. ------------------------|")
    print("|-----------------------------------------------------------|\n")
    print(f"O herói possui {vid} pontos de vida, {poc_vid} poções de vitalidade, {ouro} peças de ouro, e \
{ped_pre} pedras preciosas.\n")
    
    x += int(input("Digite a coordenada para x: "))
    y += int(input("Digite a coordenada para y: "))
    print(f"O heroi se moveu para({x},{y})")
    
    if x == 6 and y == 0 and espada1 == True:
        print("O heroi encontrou a espada sagrada, agora ele capaz de causar dano ao Tirano.")
        espada1 = False
        Espada = True
        
    if x == 6 and y == 0 and espada1 == False:
        print("Uma caverna vazia, aquilo que a tornava especial foi tirada.")
        
    if x == -2 and y == 5 and armadura == True:
        print("O herói entrou no acampamento rebelde e recebeu uma armadura!")
        vid += 900
        armadura = False
        
    if x == 9 and y == 6 and aldeia == True:
        print("O heroi invadiu a aldeia de goblins! Ele vai ser atacado!")
        
        while aldeia ==  True:
            ataque_goblin = random.randint(100, 200)
            vid -= ataque_goblin
            ac = input(f"O goblin te atacou, você está com {vid} pontos de vida, o heroi vai atacar(A), usar uma poção(B) ou irá fugir(C)?" )
            
            if ac == "A" and Espada == True:
                ataque_heroi = random.randint(150, 250)
                goblin_vida -= ataque_heroi
                print(f"O herói não se acorvadou e atacou o goblin, o goblin está com {goblin_vida} pontos de vida.")
                
            if goblin_vida <= 0:
                print("O herói derrotou o goblin, ele achou 1 peça de ouro junto ao corpo.")
                ouro += 1
                
                break;
            elif ac == "B":
                print("O herói usou uma estratégia destemida, correr.")
                break;
            
            elif ac == "C" and poc_vid != 0 and vid <= 1000:
                poc_vid -= 1
                vid += 400
                
                
                
            
    if x == 7 and y == 9 and crosta == True:
            print("O herói chegou a margem da Crosta das Sereias, ele vai ser atacado!")
            
            while crosta ==  True:
                ataque_sereia = random.randint(200, 300)
                vid -= ataque_sereia
                ac = input(f"Uma Sereia atacou o herói, e ele ficou com apenas {vid} pontos de vida o herói " )
                
                if ac == "A" and Espada == True:
                    ataque_heroi = random.randint(150, 250)
                    goblin_vida -= ataque_heroi
                    print(f"O herói não se acorvadou e atacou o goblin, o goblin está com {goblin_vida} pontos de vida.")
                    
                if goblin_vida <= 0:
                    print("O herói derrotou o goblin, ele achou 1 peça de ouro junto ao corpo.")
                    ouro += 1
                    
                    break;
            
    if x == 3 and y == 8:
        print("Vejo que você está cansado, posso te vender minhas poções de vitálidade, por 1 peça de ouro.")
        
        print(      "|------------------------------------------------------------|")
        ac = input(f"|(1)Comprar poções de vitalidade até ficar sem peças de ouro.|\n\
|(2)Ir embora.-----------------------------------------------|")
        
        if ac == 1:
            while ouro != 0:
                poc_vid +=1
                ouro -= 1
        
        
                
                
        
        
        
    if x == -2 and y == 5 and tirano == True:
        while tiranoVida > 0:
            

            print("!!! A batalha final está para começar !!!")
            
