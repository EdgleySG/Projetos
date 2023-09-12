import random
from random import randint


#INICIO DO JOGO
def player_name():
    print("************************************************************")
    nome = input("Digite o nome do seu herói: ")
    nome = nome.strip().capitalize()
    print("************************************************************")
    print("Seja bem vindo Herói {} e boa sorte no seu duelo!".format(nome))
    print("************************************************************")
    monstro = monster_name()
    luta(nome, monstro)
    return nome

#SELECIONA O OPONENTE
def monster_name():
    arquivo = open("monster.txt", "r", encoding="utf-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    monstro = palavras[numero].capitalize()
    return monstro

#INICIAR O DUELO
def luta(nome, monstro):
    print("Deseja iniciar o Duelo?\n   [1] Sim  [2] Não")
    duelo = int (input("Escolha: "))

    if (duelo == 1):
        fight = briga(nome, monstro)


    else:
        print("**********************************")
        print("Descanse e volte mais tarde!")
        print("**********************************")
    return duelo

#SCRIPT DA LUTA
def briga(nome, monstro):

    monstrohp = int(randint(21, 101))
    heroihp = int(randint(71, 91))

    print("************************************************************")
    print("O Herói {} [{}] HP desafiou {} [{}] HP\n        Para um duelo até a MORTE!!!".format(nome, heroihp, monstro, monstrohp))
    print("************************************************************")
    while (monstrohp > 0):
        print("[1] Atacar [2] Fugir [3]Implorar por sua vida")
        action = int(input("Escolha: "))

        if (action == 1):
            d6 = int(randint(0, 2))
            if (d6 > 0):
                dmg = int(randint(1, 10))
                print("************************************************************")
                print("{} Ataca e causa [{}] de dano ao {}".format(nome,dmg, monstro))
                monstrohp -= dmg
                if (dmg == 10):
                    print("     !!!CRITICAL HIT!!!")
                if (monstrohp > 1):
                    print("{} ainda tem [{}] HP.".format(monstro, monstrohp))
                    print("************************************************************")
                if (monstrohp <= 0):
                    print("O monstro foi derrotado!\n{} nosso herói vence o duelo!".format(nome))
                    print("************************************************************")
                    break
            if (d6 == 0):
                if (heroihp > 0):
                    dmg = int(randint(1, 10))
                    print("************************************************************")
                    print("Você errou o Ataque!")
                    print("{} ataca e causa [{}] de dano.".format(monstro, dmg))
                    heroihp -= dmg
                    print("{} tem [{}] pontos de vida!".format(nome, heroihp))
                    print("************************************************************")
            if (d6 > 0):
                dmg = int(randint(1, 10))
                print("{} revida e causa [{}] de dano.".format(monstro, dmg))
                heroihp -= dmg
                if (heroihp > 1):
                    print("{} ainda tem [{}] pontos de vida.".format(nome, heroihp))
                    print("************************************************************")
                if (heroihp <= 0):
                    heroihp -= 1
                    print("O herói {} perdeu o duelo para {}!\nE foi de comes e bebes!.".format(nome, monstro))
                    print("************************************************************")
                    break
        elif (action == 2):
            flee = int(randint(0, 1))
            if (flee == 1):
                print("************************************************************")
                print("{} conseguiu mandar o dibraldinho e fugiu!".format(nome))
                print("************************************************************")
                break
            else:
                print("************************************************************")
                print("{} foi mais ágil e conseguiu te acertar com toda força!\n{} morreu!".format(monstro, nome))
                print("************************************************************")
                break
        elif (action == 3):
            d6 = int(randint(0, 6))
            if (d6 == 6):
                print("************************************************************")
                print("{} implorou por sua vida e sensibilizado {} que te deixa fugir.".format(nome, monstro))
                print("************************************************************")
                break
            else:
                print("************************************************************")
                print("{} não se abalou com sua suplica e te matou!".format(monstro))
                print("************************************************************")
                break
            return fight

    print("\nFim de jogo!")

if(__name__ == "__main__"):
    player_name()