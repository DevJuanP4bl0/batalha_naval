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
    exibeEstatisticas()

def jogar()->None:
    """Função responsável pelo jogo"""
    pulaLinha()
    numJogadas = 0
    numNaviosAfundados = 0
    numSubmarinosAfundados = 0
    tabuleiro = Tabuleiro(LINHAS, COLUNAS, NAVIOS, SUBMARINOS)
    
    letras = ["A", "B", "C", "D", "E", "F"]
    numeros = ["1", "2", "3", "4", "5", "6"]

    opcoesDigitadas = []

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

            try:
                linha = letras.index(coordenada[0].upper())
                coluna = numeros.index(coordenada[1])

                if (opcao in opcoesDigitadas):
                    pulaLinha()
                    print("==> Erro: você já escolheu essa coordenada!")
                    continue

                opcoesDigitadas.append(opcao)

                embarcacao = tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna))

                if (embarcacao is None):
                    pulaLinha()
                    print("==> Água!!!!")
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, '_')
                elif (embarcacao.startswith('b')):
                    pulaLinha()
                    print("==> Návio afundado!!!!")
                    revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                    numNaviosAfundados += 1
                elif (embarcacao.startswith('s')):
                    if (tabuleiro.indiceReversoPosicoesBarcos.get((linha+1, coluna)) == embarcacao or
                        tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna+1)) == embarcacao):
                        revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, '\u2316')
                    
                    elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha-1, coluna)) == embarcacao):
                        pulaLinha()
                        print("==> Submarino afundado!!!!")
                        revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                        revelaPosicao(tabuleiro.tabuleiroOculto, linha-1, coluna, 'X')

                        numSubmarinosAfundados += 1

                    elif (tabuleiro.indiceReversoPosicoesBarcos.get((linha, coluna-1)) == embarcacao):
                        pulaLinha()
                        print("==> Submarino afundado!!!!")
                        revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna, 'X')
                        revelaPosicao(tabuleiro.tabuleiroOculto, linha, coluna-1, 'X')

                        numSubmarinosAfundados += 1

                numJogadas += 1

            except ValueError:
                print("==> Entrada inválida - Digite uma coordenada entre A 1 e F 6")
            except IndexError:
                print("==> Entrada inválida - Selecione a coluna que deseja jogar entre 1 a 6")

            if (numNaviosAfundados == NAVIOS and numSubmarinosAfundados == SUBMARINOS):
                Exibicao.exibeTabuleiro(6, 6, tabuleiro.tabuleiroOculto)
                vitoria(numJogadas)
                break

def ordenaDicionario(dicionario:dict)->dict:
    """Função responsável por organizar os dados de um dicionario com base nos valores"""

    return dict(sorted(dicionario.items(), key=lambda item: item[1]))

def estatisticas()->dict:
    """Função responsável por receber os dados lidos do arquivo"""
    jogadores = Persistencia.lerArquivo()
    dict_jogadores = {}

    for jogador in jogadores:
        dados_jogador = jogador.split()
        dict_jogadores[dados_jogador[0]] = int(dados_jogador[1])

    ranking = ordenaDicionario(dict_jogadores)

    return ranking

def exibeEstatisticas()->None:
    """Função responsável por exibir estatísticas"""
    ranking = estatisticas()

    pulaLinha()
    print("==== Melhores Pontuações ====")
    print(f'{"":<2} {"Nome":<15} {"# Jogadas":>10}')

    for posicao, (nome, pontuacao) in enumerate(ranking.items(), start=1):
        print(f'{posicao} {nome:<15} {pontuacao:>11}')
    

def menuPrincipal()->None:
    """Função que exibe o menu principal"""
    pulaLinha()
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
    elif (opcao == "2"):
        try:
            exibeEstatisticas()
        except FileNotFoundError as error:
            pulaLinha()
            print(str(error))
        except ValueError as valueError:
            pulaLinha()
            print(str(valueError))
    elif (opcao == "3"):
        break
    else:
        pulaLinha()
        print("Opção inválida!")

print("Finalizando programa")

