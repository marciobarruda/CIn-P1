# FUNÇÕES GERAIS

def qs(lista): # função quickSort: ordena uma lista, revomendo as duplicatas
    if lista==[]:
        return []
    else:
        pivor=lista[0]
        return (qs([x for x in lista if x<pivor])+[pivor]+qs([x for x in lista if x>pivor]))

def maior (lista): # função maior: devolve o maior elemento de uma lista de tuplas compostas por um inteiro e uma lista de inteiros
    
    if lista == []:
        return 'Lista vazia.'
    elif len(lista)==1: 
        return lista[0]
    else:
        x = int(len(lista[0][1]))
        y = int(len(lista[1][1]))
        if x > y: # se o tamanho da lista do elemento 0 for maior que o tamanho da lista do elemento 1, o elemento 1 é excluído
            lista.pop(1)
        elif x==y: # no caso das listas dos elementos possuírem o mesmo tamanho, o critério de desempate será o inteiro que precede a lista
            if lista[0]>lista[1]:
                lista.pop(1)
            else:
                lista.pop(0)          
        else:
            lista.pop(0)
        return maior(lista)

# 1ª QUESTÃO
# ==========
#
# A mediana de um conjunto de números N é um elemento x ∈ N que separa os elementos de N em metades superior
# (apenas com elementos maiores que x) e inferior (apenas com elementos menores que x). Se o número de elementos de N é par, 
# a mediana é a média aritmética do par de números que fica no meio. Por exemplo, a mediana do conjunto {5, 2, 3} é o número 3,
# a mediana do conjunto {8, 2, 14, 7, 4} é o número 7 e a mediana do conjunto {42, 4, 1, 7} é 5,5 (a média aritmética entre 4 e 6).
# Implementar uma função mediana() que, dada uma lista de números (sem duplicação), devolve sua mediana.


def mediana(lista): # função mediana: devolve a mediana de uma lista
    if lista==[]:
        return []
    else:
        meio=0
        lista = qs(lista)
        if len(lista)%2!=0: # no caso da lista possuir um len ímpar, devolve o elemento central
            meio = lista[int((len(lista)-1)/2)]

        else: # no caso da lista possuir um len par, delvove a média dos dois elementos centrais
            meio = (lista[int((len(lista))/2)]+lista[int((len(lista))/2)-1])/2

        return meio
    

# 2ª QUESTÃO
# ==========
#
# Construir uma função maisDivisores( ) que recebe como parâmetro uma lista de números inteiros positivos diferentes de zero e devolve,
# entre esses números, aquele que tem a maior quantidade de divisores inteiros e quais são esses divisores. Em caso de empate
# (vários números têm a maior quantidade de divisores), o programa deve escolher o maior dos números empatados. Um número x é divisor
# de um número y se o resto da divisão inteira de y por x é igual a 0. Seu programa não pode ter laços (while, for), embora possa usar 
# recursão e compreensão de listas. Aĺem disso, não deve utilizar o operador in ou funções como max, min, sum, etc. É explicitamente
# permitido, porém, criar tantas funções quanto sejam precisas (descobrir os divisores de um número, determinar qual número tem mais 
# divisores, etc.) ou usar funções da questão anterior. Exemplos de uso de maisDivisores( ) são apresentados abaixo.
#
# >>> maisDivisores([24, 5, 9, 15, 42])
# (24, [1, 2, 3, 4, 6, 8, 12, 24])
#
# >>> maisDivisores([])
# “Nenhum número.”
#
# >>> maisDivisores([1, 3, 5, 7, 11, 13, 17])
# (17, [1, 17])


def divisores(x):

    if x <= 0:
        return False
    else:
        return [y for y in range (1, x+1) if x%y==0] # retorna uma lista com todos os divisores inteiros de x

def maisDivisores(lista):

    if lista == []:
        return 'Nenhum número.'

    else:
        
        return maior(qs([(x,divisores(x)) for x in lista])) # retorna o inteiro com mais divisores de uma lista ordenada composta
                                                            # por tuplas  de inteiros e listas de divisores baseada na lista de 
                                                            # inteiros fornecida como parâmetro na função
