import Exibicao

def menuPrincipal()->None:
    """Função que exibe o menu principal"""
    print("***** Batalha Naval *****")
    print("\n")
    print("1 - Jogar")
    print("2 - Ver Melhores Pontuações")
    print("3 - Sair")

while True:
    menuPrincipal()
    Exibicao.exibeTabuleiro(6, 6)
    break

