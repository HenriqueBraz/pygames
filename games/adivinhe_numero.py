# Jogo "Advinhe o número"

import random

guessTaken = 0
print("Olá!Qual o seu nome?\n")
myName = input()
number = random.randint(1, 20)
print(f"Bem, {myName}, eu estou pensando em um número entre 1 e 20.")
while guessTaken < 6:
    print("Faça uma tentativa!")
    guess = input()
    guess = int(guess)
    guessTaken += 1
    if guess < number:
        print("Sua tentativa foi muito baixa.")
    elif guess > number:
        print("Sua tentativa foi muito alta.")
    else:
        break


if guess == number:
    guessTaken = str(guessTaken)
    print(f"Bom trabalho, {myName}! Você acertou o número em {guessTaken} tentativas!")
elif guess != number:
    number = str(number)
    print(f"Que pena! O número que eu estava pensando era {number}.")