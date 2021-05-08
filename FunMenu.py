from CORES import cores
from CORES import semcor


def leiaint(msg):   
    import CORES
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print()
            CORES.cores(4)
            print('ERRO: por favor, digite um número inteiro válido')
            CORES.semcor()
            continue
        except Exception as ERRO:
            print()
            CORES.cores(4)
            print(f'Um problema foi encontrado, digite um número inteiro válido :(')
            CORES.semcor()
            continue
        else:
            return n

def linha(tam = 42):
    return '-'*tam



def cabeçalho(txt):
    cores(3)
    print(linha())
    cores(2)
    print(txt.center(42))
    cores(3)
    print(linha())
    semcor()
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        cores(3)
        print(f'{c} - ',end='')
        cores(2)
        print(f'{item}')
        semcor()
        c += 1
    cores(3)
    print('='*42)
    semcor()
    opc = leiaint('-------> Sua Opção: ')
    return opc


    


