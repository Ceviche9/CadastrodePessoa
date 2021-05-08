from FunMenu import *
from CORES import *
def arquivoExiste(arq):
    try:
        a = open(arq, 'rU')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'O arquivo {arq} foi criado com sucesso')

def LerArquivo(arq):
    try:
       a = open(arq, 'r')
    except:
        cores(4)
        print('Erro ao tentar ler o arquvio')
        semcor()
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            print(linha)
        a.close()

def Cadastrar(arq, nome='Desconhecido', idade='0'):
    try:
        a = open(arq, 'a')
    except:
        print()
        cores(4)
        print('Erro! Não foi possível Cadastrar Novo Usuário')  
        semcor()
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos\n')
        except:
            print()
            cores(4)
            print('ERRO! Não foi possivel cadastrar novo usuário')
            semcor()
        else:
            print()
            cores(6)
            print(f'Novo registro de {nome} atualizaado')
            semcor()
            a.close()

def Apagar(arq):
    try:
        a = open(arq, 'w')
    except:
        print()
        cores(4)
        print('Erro! Não foi possível apagar um usuário')
        semcor()
    else:
        cabeçalho('DADOS DE USUÁRIOS APAGADOS ')
        a.close() 




               

     


