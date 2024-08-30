import random

welcome_gamer = input("Estou animada para jogar com você 🤓\nPara Começar escreva seu primeiro nome: ")

print(f'Boa {welcome_gamer}. Lets Goo! 🦖')


your_score = 0
my_score = 0

valid_choices = ["pedra", "papel", "tesoura"]

while True:
    gamer = input("Para começar digite: papel, tesoura ou pedra (ou 'sair' para encerrar): ").lower()
    if gamer not in valid_choices:
        print("Entrada inválida. Por favor, digite apenas 'pedra', 'papel' ou 'tesoura'.")
        continue
    gamer_random = random.choice(["pedra", "papel", "tesoura"])
    
    
    if gamer == "sair":
        print("Jogo encerrado. Obrigado por jogar!")
        print(f"Placar final: Você {your_score} x {my_score} IA")
        break
    
    
    if gamer_random ==  gamer:
        print("Deu empate")
    elif gamer_random == "tesoura" and gamer == "papel":
        print(f"Meu resultado foi {gamer_random}. Cortei seu {gamer} ")
        my_score +=1
    elif gamer_random == "pedra" and gamer == "tesoura":
        print(f"Meu resultado foi {gamer_random}.  Amassei e  quebrei sua {gamer}")
        my_score +=1
    elif gamer_random == "papel" and gamer == "pedra":
        print(f"Meu resultado foi {gamer_random}.  Embrulhei sua {gamer}")
        my_score +=1
    else:
        print(f"Tirei {gamer_random}, você ganhou 🎈🎈🎈")
        your_score+=1


    print(f"Placar: Você {your_score} x {my_score} IA\n")
    
