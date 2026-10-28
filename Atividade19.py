# Use o print() para mostrar o preço de uma poção (10 moedas)
# Use o input() para perguntar quantas poções o jogador quer.
# Calcule o total e use o print() para mostrar o valor da fatura.

pocao_valor = 15
moedas = 90

print(f" A poção está na promoção, ela está saindo por {pocao_valor}.\n \
O jogador possui {moedas}.")

total = int(input("Quantas poções deseja comprar?"))

compras = total * pocao_valor

if compras <= moedas:
    moedas -= compras
    
    print(f"Compras feitas com sucesso, você ficou com {moedas} moedas.")

else:
    print("Você não tem moedas o suficiente.")
