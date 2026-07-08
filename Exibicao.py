#caracteres utilizados

def mostrarCaracteresUsados():
  print('O caractere _ é usado para água')
  print('O caractere X é usado para embarcação afundada')
  print('O caractere \u2316 é usado para embarcação parcialmente atingida')
  print('O caractere \u2588 é usado para denotar posição ainda não exploradas do tabuleiro')

def exibeTabuleiro(linhas:int, colunas:int, tabuleiro:list)->None:
  print("\n")
  print("   ", end="")
  letras = ["A", "B", "C", "D", "E", "F"]

  for i in range(1, colunas+1):
    print(f"{i:^3}", end="")
    
  print()

  for i in range(linhas):
    print(f"{letras[i]} |", end="")
    for j in range(colunas):
        print(f'{tabuleiro[i][j]:^3}', end="")
    print("\n")
  
  print()

if __name__ == "__main__":
  exibeTabuleiro()