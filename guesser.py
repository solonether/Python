#!/usr/bin/python3

import random

numero = random.randrange(1000)
while True:
    v = int(input())
    if numero == v:
        print('Hai vinto!')
        break
    print('Minore' if (numero < v) else 'Maggiore')