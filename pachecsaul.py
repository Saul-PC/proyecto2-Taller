import time
t0 = time.time()
def encontrarCoords(M):
    res = []
    char = ""
    for i in range(len(M[0])):
        for j in range(len(M)):
            if M[i][j] != ".":
                res.append((i,j))
                char = M[i][j]
    return res,char


def espejo(M):
    mEsp = [["." for i in range(len(M))] for j in range(len(M[0]))]
    for i in range(len(M[0])):
        mEsp[i] = M[i][::-1]
    return mEsp


def rotacion(M,indice):
    n = len(M)
    m = len(M[0])

    res = [["." for _ in range(m)]for _ in range(n)]

    if indice == 0:
        return M

    for i in range(m):
        for j in range(n):
            res[j][n-1-i] = M[i][j]
    return rotacion(res,indice-1)


def esquinaMat(M):
    matEsquina = [["." for _ in range(len(M))] for _ in range(len(M[0]))]
    XY = []
    char = "."
    for i in range(len(M[0])):
        for j in range(len(M)):
            if M[i][j] != ".":
                XY.append((i,j))
                char = M[i][j]
    
    if XY == []:
        return M

    listaX = []
    listaY = []
    res = []

    for x,y in XY:
        listaX.append(x)
        listaY.append(y)

    mnX = min(listaX)
    mnY = min(listaY)

    for x,y in XY:
        x -= mnX
        y -= mnY
        res.append((x,y))
    
    for i,j in res:
        matEsquina[i][j] = char
    return matEsquina


def insertarCoords(M,XY,char):
    matValida = [["." for i in range(len(M[0]))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            matValida[i][j] = M[i][j]

    for x,y in XY:
        matValida[x][y] = char
    return matValida


def esSimetrico(M):
    M = esquinaMat(M)
    mEsp = esquinaMat(espejo(M))
    for i in range(len(M[0])):
        for j in range(len(M)):
            if M[i][j] != mEsp[i][j]:
                return False
    return True


def piezaJusta(M):
    if M == [["." for i in range(len(M))] for j in range(len(M[0]))]:
        return M
    
    matAux = [["." for i in range(len(M))] for j in range(len(M[0]))]
    for i in range(len(M[0])):
        for j in range(len(M)):
            matAux[i][j] = M[i][j]
    
    coords,char = encontrarCoords(esquinaMat(matAux))

    listaX = []
    listaY = []

    for x,y in coords:
        listaX.append(x)
        listaY.append(y)

    maxX = max(listaX)
    maxY = max(listaY)

    matJusta = [["." for i in range(maxY+1)] for j in range(maxX+1)]

    for x,y in coords:
        matJusta[x][y] = char
    return matJusta


def hijosNada(tablero,piezas,indice,L,A):
    hijos = []

    if indice == len(piezas):
        return hijos
    
    pieza = esquinaMat(piezas[indice])

    XY,char = encontrarCoords(pieza)

    validCoords = []

    for i in range(L):
        for j in range(A):
            for x,y in XY:
                if x + i >= 0 and x + i < L and y + j >= 0 and y + j < A:
                    if tablero[i+x][j+y] != ".":
                        validCoords = []
                        break
                        
                    validCoords.append((i+x,j+y))

                else:
                    validCoords = []
                    break
                    
            if validCoords != []:
                nuevoHijo = insertarCoords(tablero,validCoords,char)
                hijos.append((nuevoHijo,indice+1))
                validCoords = []

    return hijos


def hijosRots(tablero,piezas,indice,L,A):
    hijos = []

    if indice == len(piezas):
        return hijos
    
    pieza = piezas[indice]

    for rot in range(4):
        pRot = esquinaMat(rotacion(pieza,rot))

        XY,char = encontrarCoords(pRot)

        validCoords = []

        for i in range(L):
            for j in range(A):
                for x,y in XY:
                    if x + i >= 0 and x + i < L and y + j >= 0 and y + j < A:

                        if tablero[i+x][j+y] != ".":
                            validCoords = []
                            break
                        
                        validCoords.append((i+x,j+y))

                    else:
                        validCoords = []
                        break
                    
                if validCoords != []:
                    nuevoHijo = insertarCoords(tablero,validCoords,char)
                    hijos.append((nuevoHijo,indice+1))
                    validCoords = []


    return hijos


def hijosTodo(tablero,piezas,indice,L,A):
    hijos = []

    if indice == len(piezas):
        return hijos
    
    pieza = piezas[indice]

    for rot in range(4):
        pRot = esquinaMat(rotacion(pieza,rot))

        XY,char = encontrarCoords(pRot)

        validCoords = []

        for i in range(L):
            for j in range(A):
                for x,y in XY:
                    if x + i >= 0 and x + i < L and y + j >= 0 and y + j < A:

                        if tablero[i+x][j+y] != ".":
                            validCoords = []
                            break
                        
                        validCoords.append((i+x,j+y))

                    else:
                        validCoords = []
                        break
                    
                if validCoords != []:
                    nuevoHijo = insertarCoords(tablero,validCoords,char)
                    hijos.append((nuevoHijo,indice+1))
                    validCoords = []
                
                

    piezaEsp = espejo(pieza)

    for rot in range(4):
        pEsp = esquinaMat(rotacion(piezaEsp,rot))

        XY,char = encontrarCoords(pEsp)

        validCoords = []

        for i in range(L):
            for j in range(A):
                for x,y in XY:
                    if x + i >= 0 and x + i < L and y + j >= 0 and y + j < A:

                        if tablero[i+x][j+y] != ".":
                            validCoords = []
                            break
                        
                        validCoords.append((i+x,j+y))

                    else:
                        validCoords = []
                        break
                    
                if validCoords != []:
                    nuevoHijo = insertarCoords(tablero,validCoords,char)
                    hijos.append((nuevoHijo,indice+1))
                    validCoords = []
    return hijos


def buscarHijos(tablero,piezas,indice,L,A):

    if esSimetrico(piezas[indice]):

        if piezaJusta(piezas[indice]) == rotacion(piezaJusta(piezas[indice]),1):

            return hijosNada(tablero,piezas,indice,L,A)
        
        return hijosRots(tablero,piezas,indice,L,A)
    
    return hijosTodo(tablero,piezas,indice,L,A)


def matrices(P):
    string = ""
    lista = []
    char = []
    cont = 1
    contLista = 0
    mats = []

    for i in range(P*4):
        string = input()

        for j in string:
            char += [j]

            if cont % 4 == 0:
                lista.append(char)
                char = []
                contLista += 1

                if contLista % 4 == 0:
                    mats.append(lista)
                    lista = []
                    
            cont += 1

    return mats


def juego(piezas,L,A): 
    pila = [([["." for i in range(A)] for j in range(L)],0)]

    while pila:
        tablero,indice = pila.pop()

        if indice == len(piezas):
            for i in range(L):
                for j in range(A):
                    if tablero[i][j] == ".":
                        return "No se encontró solución"
            return tablero
        
        hijos = buscarHijos(tablero,piezas,indice,L,A)

        for i in hijos:
            pila.append(i)
    return "No se encontró solución"



L,A,P = map(int, input().split())

mats = matrices(P)

print(juego(mats,L,A))
t1 = time.time()
print(t1-t0)


