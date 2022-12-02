# Jogo "No Reino dos Dragões"

import os
import random
import time


def display_intro():
    os.system('clear') or None
    print("Você está em uma ilha cheia de dragões. Em frente a você,")
    print("está duas cavernas. Em uma, o dragão é amigável e repartirá")
    print("o seu tesouro com você. O outro dragão porém é ganancioso e")
    print("faminto, e vai devorar você em um segundo.")

def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Qual caverna você vai entrar? (1 ou 2)")
        cave = input()
    return cave

def check_cave(chosenCave):
    print("Você se aproxima da caverna...")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("Está escuro e sombrio....")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print()
    print("Um enorme dragão surge na sua frente! Ele abre a sua enorme mandíbula e ...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    friendly_cave = str(random.randint(1, 2))
    if chosenCave == friendly_cave:
        print("Entrega o tesouro dele com um sorriso simpático! Você sobreviveu e ainda ficou rico! :)")
    else:
        print("Engole você de uma só vez... pena, você morreu /:")

playAgain = 'sim'
while playAgain == 'sim' or playAgain == 's':
    display_intro()
    caveNumber = choose_cave()
    check_cave(caveNumber)
    print("Você quer jogar de novo? (sim ou não)")
    playAgain = input()



