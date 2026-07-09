def gravaArquivo(nome:str, numJogadas:str)->None:
    """Função responsável por gravar vencedores em um arquivo"""
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(f'{nome} {numJogadas}\n')


def lerArquivo()->list:
    """Função responsável por ler os vencedores em um arquivo"""
    with open('ranking.txt', 'r') as arquivo:
        jogadores = arquivo.readlines()

    return jogadores