def gravaArquivo(nome:str, numJogadas:str)->None:
    """Função responsável por gravar vencedores em um arquivo"""
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(f'{nome} {numJogadas}\n')


def lerArquivo()->list:
    """Função responsável por ler os vencedores em um arquivo"""
    try:
        with open('ranking.txt', 'r') as arquivo:
            jogadores = arquivo.readlines()
            if (len(jogadores) == 0):
                raise ValueError("Ranking indisponível: não há jogadores para rankear!")
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo ranking.txt inexistente: jogue uma vez para gerar o arquivo!")

    return jogadores