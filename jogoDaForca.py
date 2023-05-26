
import random
#temas
carros = ["MAZDA","VOLSKWAGEN","BUGATTI","HONDA","NISSAN","TOYOTA","FERRARI","FORD","CHEVROLET","MERCEDES"]
frutas = ["MORANGO","BANANA","MAÇÃ","MELANCIA","MELÃO","LIMÃO","LARANJA","KIWI"]
chave1 = []
posicao = 0
chave2 = []
tentativas = 7
acertos = 0
palavraSorteada = None
tema = int(input("Escolha um tema:\n1.FRUTAS\n2.CARROS\n"))
while tema != 1 and tema != 2:
    print("Opção inválida!")
    tema = int(input("Escolha um tema:\n1.FRUTAS\n2.CARROS\n"))

match tema:
    case 1:
        palavraSorteada = random.choice(frutas)
    case 2:
        palavraSorteada = random.choice(carros)

for x in palavraSorteada:
    chave1.append(x)
    posicao+=1
    chave2.append(' ')
print(chave2)

while True:

    letra = str.upper(input("Digite uma letra: "))
    if letra in palavraSorteada:
        for x in range(posicao):
            if letra == chave1[x]:
                del chave2[x]
                chave2.insert(x, letra)
                acertos+=1
    else:
        tentativas-=1
        if tentativas>-1:
            print(f"resposta incorreta você tem: {tentativas} tentativas")

    print(chave2)


    if chave1 == chave2:
        tentativas = 7
        print("Parabéns! Certa resposta.")
        repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
        while repetir != 1 and repetir != 2:
            print("Digite uma opção válida!")
            repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
        if repetir == 1:
            for x in range(posicao):
                    del chave2[x]
                    chave2.insert(x, ' ')
                    acertos = 0
        else:
            acertos = 0
            break

    if tentativas<0:
        print("GAME OVER")
        repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
        while repetir != 1 and repetir != 2:
            print("Digite uma opção válida!")
            repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
        if repetir == 1:
            tentativas = 7
            for x in range(posicao):
                if letra == chave1[x]:
                    del chave2[x]
                    chave2.insert(x, ' ')
        else:
            break

    if acertos>1:
        resp = int(input("Ja sabe a palavra? 1.SIM   2.NÃO"))
        while resp != 1 and resp != 2:
            print("Opção inválida!")
            resp = int(input("Ja sabe a palavra? 1.SIM   2.NÃO"))
        if resp == 1:
            tentativas = 7
            check = str.upper(input("Digite a palavra: "))
            if check == palavraSorteada:
                print("Parabéns! Certa resposta.")
                repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
                while repetir != 1 and repetir != 2:
                    print("Digite uma opção válida!")
                    repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
                if repetir == 1:
                    acertos = 0
                    for x in range(posicao):
                            del chave2[x]
                            chave2.insert(x, ' ')
                else:
                    break
            else:
                tentativas = 7
                acertos = 0
                print("GAME OVER")
                repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
                while repetir != 1 and repetir != 2:
                    print("Digite uma opção válida!")
                    repetir = int(input("Deseja jogar novamente? 1.SIM   2.NÃO"))
                if repetir == 1:
                    for x in range(posicao):
                        if letra == chave1[x]:
                            del chave2[x]
                            chave2.insert(x, ' ')
                else:
                    break