
c = ('\033[m',          # 0- Sem cor 
     '\033[1m',        # 1- Letras em Negrito
     '\033[0;34m',      # 2- Letras en Azul
     '\033[0;33m',     # 3- Letras em amarelo?
     '\033[0;31m',    # 4- Letras em Vermelho
     '\033[42m',      # 5- Fundo verde
     '\033[46m',      # 6- Fundo Ciano
     '\033[0;0;40m',   # 7- Fundo Branco
     '\033[0;0;41m',   # 8- Fundo Vermelho
     '\033[' 
         )

def cores(cor=0):
    print(c[cor], end='')

def semcor(cor=0, end=''):
    print(c[0])
