import forca
import advinhcao
def escolhe_jogo():
    print("********************************")
    print("Bem vindo! Escolha o seu jogo:")
    print("********************************")

    print("(1) Jogo da Forca (2) Jogo de Advinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando jogo da advinhação")
        advinhcao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()