import random

print("Vamos jogar pedra, papel, tesoura!")

player = input("Qual o nome do jogador?\n")

optBot = int(input("Deseja dar um nome para o bot?\n(1) - Sim\n(2) - Não\n"))
if optBot == 1:
    nomeBot = input("Qual o nome do bot?\n")
else:
    nomeBot = "Bot"

contBot = 0
contPlayer = 0
jogo = ["Pedra", "Papel", "Tesoura"]

resposta = 0

while(resposta!=-4):
    resposta = int(input("(1) - Pedra\n(2) - Papel\n(3) - Tesoura\n(4) - Sair\n"))
    bot = random.choice(jogo)
    if resposta!=4:
        print(f"{nomeBot}: {bot}")
    if resposta == 1:
        print(f"{player}: Pedra")
        if bot == "Papel":
            print(f"{nomeBot} ganhou a rodada!")
            contBot += 1
        elif bot == "Tesoura":
            print(f"{player} ganhou a rodada!")
            contPlayer += 1
        else:
            print("Empate!")
    elif resposta == 2:
        print(f"{player}: Papel")
        if bot == "Pedra":
            print(f"{player} ganhou a rodada!")
            contPlayer += 1
        elif bot == "Tesoura":
            print(f"{nomeBot} ganhou a rodada!")
            contBot += 1
        else:
            print("Empate!")
    elif resposta == 3:
        print(f"{player}: Tesoura")
        if bot == "Papel":
            print(f"{player} ganhou a rodada!")
            contPlayer += 1
        elif bot == "Pedra":
            print(f"{nomeBot} ganhou a rodada!")
            contBot += 1
        else:
            print("Empate!")
    else:
        break
    print(f"----Placar----\n{player}: {contPlayer} vs {nomeBot}: {contBot}")

if contPlayer == contBot:
    print("Empatou!")
elif contPlayer > contBot:
    print(f"{player} ganhou o jogo!")
else:
    print(f"{nomeBot} ganhou o jogo!")


