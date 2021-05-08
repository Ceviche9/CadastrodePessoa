from FunMenu import *
from Arquivo import *
from CORES import *
from time import sleep


arq = 'Dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar NovOs Usuários','Apagar Usuários','Sair do Sistema'])
    if resposta ==1:
        #Opção de listar o conteúdo de um arquivo.
        LerArquivo(arq)
    elif resposta ==2:
        #Opção para cadastrar novos usuários.
        cabeçalho('CADASTRAR NOVO USUÁRIO')
        Nome = str(input('Nome: '))
        Idade = int(input('Idade: '))
        Cadastrar(arq, Nome, Idade)
    elif resposta ==3:
        Apagar(arq)
    elif resposta ==4:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(0.75)
        break
    else:
        print()
        cores(4)
        print('Erro! Digite uma opção válida')
        semcor()






