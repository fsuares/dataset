
from functions import *
from time import sleep
import numpy as np

def main():
    temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
        6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
        8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
        10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
        7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
        6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
        5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
        6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
        9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
        10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

    mais_frio = np.argmin(temperaturas) + 1
    mais_quente = np.argmax(temperaturas) + 1
    temp_mais_frio = np.min(temperaturas)
    temp_mais_quente = np.max(temperaturas)
    frios = []
    quentes = []
    moderado = []

    variancia = np.var(temperaturas)
    mediana = np.median(temperaturas)
    media = np.average(temperaturas)
    desvio = np.std(temperaturas)

    print('\n1) Media/Mediana')
    print('Média : {}'.format(round(media, 2)))
    sleep(0.5)
    print('Mediana: {}'.format(round(mediana, 2)))
    sleep(0.5)
    print('Variância: {}'.format(round(variancia, 2)))
    sleep(0.5)
    print('Desvio Padrão: {}'.format(round(desvio, 2)))
    sleep(0.5)

    for i in range(len(temperaturas)):
        if temperaturas[i] < 5:
            frios.append(i)
        elif temperaturas[i] >= 5 and temperaturas[i] <= 15:
            moderado.append(i)
        elif temperaturas[i] > 15:
            quentes.append(i)


    print('\n2) Agrupamento')
    sleep(0.5)
    print('Dias Frios:')
    sleep(0.5)
    for i in range(len(frios)):
        print('{}º|'.format(frios[i]+1), end='')

    print('\n')
    print('Dias Moderados:')
    sleep(0.5)
    for i in range(len(moderado)):
        print('{}º|'.format(moderado[i]+1), end='')

    print('\n')
    print('Dias Quentes:')
    sleep(0.5)
    for i in range(len(quentes)):
        print('{}º|'.format(quentes[i]+1), end='')

    print('\n3) Extremos')
    print('Dia mais quente: {}º dia com uma temperatura de {}°C'.format(mais_quente, temp_mais_quente))
    sleep(0.5)
    print('Dia mais frio: {}º dia com uma temperatura de {}°C'.format(mais_frio, temp_mais_frio))


if __name__ == '__main__':
    main()

