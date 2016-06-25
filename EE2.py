# 1ª QUESTÃO
# ==========

def qs(lista):
    if lista==[]:
        return []
    else:
        pivor=lista[0]
        return (qs([x for x in lista if x<pivor])+[pivor]+qs([x for x in lista if x>pivor]))

def mediana(lista):
    if lista==[]:
        return []
    else:
        meio=0
        lista = qs(lista)
        if len(lista)%2!=0:
            meio = lista[int((len(lista)-1)/2)]

        else:
            meio = (lista[int((len(lista))/2)]+lista[int((len(lista))/2)-1])/2

        return meio
    

# 2ª QUESTÃO
# ==========

def listaDivisores(lista):
    if lista == []:
        return []
    else:
        lista=qs(lista)
        resultado=[]
        resultado.append((lista[0],[y for y in range(1,((lista[0])+1)) if (int(lista[0]))%y==0]))
        return resultado+listaDivisores(lista[1:])
    return listaDivisores(lista)

    
def maisDivisores(lista):

    if len(lista)==[]:
        return "Nenhum número."

    else:
        if int(len(lista))==1:
            return lista[0]
        elif int(len(lista[0][1]))<int(len(lista[1][1])):
            lista.pop(0)
        elif int(len(lista[0][1]))==int(len(lista[1][1])):
            if lista[0]<lista[1]:
                lista.pop(0)
            else:
                lista.pop(1)
        else:
            lista.pop(1)
        return maisDivisores(lista)
    return lista
