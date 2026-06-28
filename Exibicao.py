from Tabuleiro import Tabuleiro

#caracteres utilizados

def mostrarCaracteresUsados():
  print('O caractere _ é usado para água')
  print('O caractere X é usado para embarcação afundada')
  print('O caractere \u2316 é usado para embarcação parcialmente atingida')
  print('O caractere \u2588 é usado para denotar posição ainda não exploradas do tabuleiro')

def exibeTabuleiro():
  linhas  = 6
  colunas = 6 
  sep = '  '
  for i in range(linhas):
    for j in range(colunas):
        print('\u2588', end=sep)
    print()

if __name__ == "__main__":
  exibeTabuleiro()