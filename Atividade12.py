#Crie um código que pergunte: "Deseja salvar o progresso? (S/N" e apenas exiba no console a resposta digitada.

salvar = str(input("Deseja salvar o progresso(S/N):"))

if salvar == "S":
    print("O sistema será salvo.")
    
elif salvar == "N":
    print("O progresso será perdido.")
    
else: 
    print("Resposta inválida, perdendo o progresso.")
