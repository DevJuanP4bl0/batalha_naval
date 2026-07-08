import Exibicao
from Tabuleiro import Tabuleiro

LINHAS = 6
COLUNAS = 6
NAVIOS = 5
SUBMARINOS = 3

def pulaLinha()->None:
    """Função responsável por pular linhas"""
    print("\n")

def jogar()->None:
    """Função responsável pelo jogo"""
    pulaLinha()
    numJogadas = 0
    numNaviosAfundados = 0
    numSubmarinosAfundados = 0
    tabuleiro = Tabuleiro(LINHAS, COLUNAS, NAVIOS, SUBMARINOS)
    
    letras = ["A", "B", "C", "D", "E", "F"]
    numeros = ["1", "2", "3", "4", "5", "6"]


    while True:
        Exibicao.exibeTabuleiro(6, 6, tabuleiro.tabuleiroOculto)
        print(f'Jogadas até agora: {numJogadas}')
        print(f'Afundados até agora = Navios {numNaviosAfundados} de {NAVIOS} | ', end="")
        print(f'Submarinos {numSubmarinosAfundados} de {SUBMARINOS}')
        print("Digite a posição para tentar (formato linha coluna)")
        opcao = input(" Se quiser desistir digite -1: ")

        if (opcao == "-1"):
            break
        else:
            coordenada = opcao.split()

            linha = letras.index(coordenada[0])
            coluna = numeros.index(coordenada[1])

            embarcacao = tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna))

            if (embarcacao is None):
                print("AGUAAA")
                tabuleiro.tabuleiroOculto[linha][coluna] = "_"
            elif (embarcacao.startswith('b')):
                print("É BARCOOO")
                tabuleiro.tabuleiroOculto[linha][coluna] = "X"
                numNaviosAfundados += 1
            elif (embarcacao.startswith('s')):
                if (tabuleiro.indiceReversoPosicoesBarcos.get((linha+1, coluna)) == embarcacao or
                    tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna+1)) == embarcacao):
                    tabuleiro.tabuleiroOculto[linha][coluna] = "O"
                
                elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha-1, coluna)) == embarcacao):
                    tabuleiro.tabuleiroOculto[linha][coluna] = "X"
                    tabuleiro.tabuleiroOculto[linha-1][coluna] = "x"

                    numSubmarinosAfundados += 1

                elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna-1)) == embarcacao):
                    tabuleiro.tabuleiroOculto[linha][coluna] = "X"
                    tabuleiro.tabuleiroOculto[linha][coluna-1] = "x"

                    numSubmarinosAfundados += 1

            numJogadas += 1

def menuPrincipal()->None:
    """Função que exibe o menu principal"""
    print("***** Batalha Naval *****")
    pulaLinha()
    print("1 - Jogar")
    print("2 - Ver Melhores Pontuações")
    print("3 - Sair")

while True:
    menuPrincipal()
    opcao = input("Escolha uma opção: ")

    if (opcao == "1"):
        jogar()
    break

