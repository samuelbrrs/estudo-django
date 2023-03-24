import random

numero = random.randint(1, 100)
tentativas = 0

print("Eu estou pensando em um número entre 1 e 100. Você tem 7 tentativas para adivinhar.")

while tentativas < 7:
    tentativas += 1
    palpite = int(input("Tentativa {}: Qual é o seu palpite? ".format(tentativas)))
    
    if palpite < numero:
        print("O número que eu estou pensando é maior do que {}".format(palpite))
    elif palpite > numero:
        print("O número que eu estou pensando é menor do que {}".format(palpite))
    else:
        print("Parabéns! Você acertou o número em {} tentativas.".format(tentativas))
        break

if tentativas == 7:
    print("Infelizmente, você usou todas as suas tentativas. O número correto era {}.".format(numero))
    