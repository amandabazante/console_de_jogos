def jogar_adivinhacao():
    alvo = 25
    chances = 5
    acertou = False

    while chances > 0 and not acertou:
      try:
        chute = int(input("Digite um número inteiro entre 0 e 100 - "))
        chances-=1

        if chute == alvo:
            print("Parabéns! Adivinhou o número!")
            acetou = True
        else:
            if chute > alvo:
                print("Não acertou! O número é menor que o seu palpite")
            else:
                print("Não acertou! O número é maior que o seu palpite")
            

      except:
        print("Tente Novamente!")

    if not acertou:
        print("Que pena, o número era - ", + alvo)

def jogar_jokenpo():
    jogador1 = int(input("Jogador1, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    jogador2 = int(input("Jogador2, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    pedra = 0
    papel = 1
    tesoura = 2
    if (jogador1 == jogador2):
     print("Empate! Ninguém ganhou.")
    elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
     print("Jogador 1 ganhou.")
    else:
     print("Jogador 2 ganhou.") 
    jogador1 = int(input("Jogador1, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    jogador2 = int(input("Jogador2, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    pedra = 0
    papel = 1
    tesoura = 2
    if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
     if (jogador1 == jogador2):
      print("Empate! Ninguém ganhou.")
     elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
      print("Jogador 1 ganhou.")
     else:
      print("Jogador 2 ganhou.")
    else:
      print("Opção inválida.")

def jogar_quiz():
    
    print("Qual a capital do Brasil? a) Brasilia b) Rio de Janeiro c) São Paulo d) Recife")
    resposta = input("Escolha a alternativa correta: ")
    if resposta == ("a"):
     print("Você acertou")
    else:
     print("Você errou")

    print("Quantos dentes temos na boca? a) 25 b) 30 c) 32 d) 35")
    resposta = input("Escolha a alternativa correta: ")
    if resposta == ("c"):
     print("Você acertou")
    else:
     print("Você errou")


    print("Olá, seja bem vindo!")
    print("Cada pergunta terá um valor determinado!")
    print("Segue os valores:")
    print("A primeira pergunta vale 20 pontos!")
    print("A segunda pergunta vale 10 pontos!")

    perguntas = ["Qual a capital do Brasil?" , "Quantos dentes temos na boca?"]
    respostas = ["Brasília" , "32"]
    pontuacao = 0
    respostas_corretas = 0

    for pergunta in perguntas:
        print(pergunta)
        resposta_usuario = str(input('Qual sua resposta?: '))
        for resposta in respostas:
          if resposta_usuario == resposta:
            respostas_corretas += 1
    pontos = respostas_corretas * 20 + 10

    print('Você acertou {} perguntas e sua pontuação é {}'.format(respostas_corretas, pontos))

print('''Bem Vindo ao Console de Jogos!!!
Menu principal:
1 - Jogo de Adivinhação
2 - Jogo de Jokenpo
3 - Jogo do Quiz
0 - Sair
''')

jogo_em_andamento = True

while jogo_em_andamento:
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


  