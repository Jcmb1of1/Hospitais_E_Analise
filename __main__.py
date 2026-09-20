from classes import *


def main():
    obj_1 = Analise('Leitos_2026.csv')
    obj_2 = Consultas('Leitos_2026.csv')
    obj_1.estabelecimentos_por_estado()

if __name__ == '__main__':
    main()
