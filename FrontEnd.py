import Exibicao
from Tabuleiro import Tabuleiro

def menuPrincipal()->None:
    """Função que exibe o menu principal"""
    print("***** Batalha Naval *****")
    print("\n")
    print("1 - Jogar")
    print("2 - Ver Melhores Pontuações")
    print("3 - Sair")

while True:
    tabuleiroOculto = Tabuleiro(6, 6, 3, 5)
    menuPrincipal()
    Exibicao.exibeTabuleiro(6, 6, tabuleiroOculto.tabuleiroOculto)
    break

