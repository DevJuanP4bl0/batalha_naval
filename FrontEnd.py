import Exibicao
from Tabuleiro import Tabuleiro
import Persistencia

LINHAS = 6
COLUNAS = 6
NAVIOS = 5
SUBMARINOS = 3

def pulaLinha()->None:
    """Função responsável por pular linhas"""
    print("\n")

def revelaPosicao(tabuleiro:list, linha:int, coluna:int, caractere:str)->None:
    """Função responsável por revelar as posições."""
    tabuleiro[linha][coluna] = caractere

def vitoria(numJogadas:int)->None:
    """Função responsável caso a pessoa vença"""
    pulaLinha()
    print("***** Você ganhou!!!!!! *****")
    pulaLinha()
    print("Melhores pontuações")
    nome = input("Digite seu nome: ")
    Persistencia.gravaArquivo(nome, numJogadas)
    pulaLinha()

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
                revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, '_')
            elif (embarcacao.startswith('b')):
                revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                numNaviosAfundados += 1
            elif (embarcacao.startswith('s')):
                if (tabuleiro.indiceReversoPosicoesBarcos.get((linha+1, coluna)) == embarcacao or
                    tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna+1)) == embarcacao):
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, '\u2316')
                
                elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha-1, coluna)) == embarcacao):
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha-1, coluna, 'X')

                    numSubmarinosAfundados += 1

                elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna-1)) == embarcacao):
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna-1, 'X')

                    numSubmarinosAfundados += 1

            numJogadas += 1

            if (numNaviosAfundados == NAVIOS and numSubmarinosAfundados == SUBMARINOS):
                vitoria(numJogadas)
                input()

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

