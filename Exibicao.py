#caracteres utilizados

def mostrarCaracteresUsados():
  print('O caractere _ é usado para água')
  print('O caractere X é usado para embarcação afundada')
  print('O caractere \u2316 é usado para embarcação parcialmente atingida')
  print('O caractere \u2588 é usado para denotar posição ainda não exploradas do tabuleiro')

def exibeTabuleiro(linhas:int, colunas:int):
  print("\n")
  print("   ", end="")

  for i in range(1, colunas+1):
    print(f"{i:^3}", end="")
    
  print()

  for letra in "ABCDEF":
    print(f"{letra} |", end="")
    for j in range(linhas):
        print(f'{"\u2588":^3}', end="")
    print("\n")
  
  print()

if __name__ == "__main__":
  exibeTabuleiro()