def jogar_adivinhacao():
    print("adivinhacao")

def jogar_jokenpo():
    print("jokenpo")

def jogar_quiz():
    print("quiz")

print('''Bem Vindo ao Console de Jogos!!!
Menu principal:
1 - Jogo de Adivinhação
2 - Jogo de Jokenpo
3 - Jogo do Quiz
0 - Sair
''')

codigo_jogo = input("Qual jogo você deseja jogar? ")

if codigo_jogo == "1":
  jogar_adivinhacao()
elif codigo_jogo == "2":
  jogar_jokenpo()
elif codigo_jogo == "3":
  jogar_quiz()
elif codigo_jogo == "0":
  print("Programa encerrado! Até mais!")
else: 
  print("Opção inválida")