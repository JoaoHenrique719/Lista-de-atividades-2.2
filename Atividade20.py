#Identifique o erro de sintaxe ou lógica no código abaixo:
#O objetivo é ler o nome e dar boas vindas

#O problema do código é que ele inverte as funções de print e input.
#A variável print só mostra o que está escrito, e não abre espaço para o usuário digitar.
nome = print("Digite seu nome:")
#Já no imput, ele vai mostrar a mensagem principal e a variável "nome" e , logo após, vai abrir a opção de digitar.
input("Bem vindo", nome)
