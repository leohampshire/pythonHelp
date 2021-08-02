
#n é sempre ímpar, então há uma posição central de cada matriz (3x3 - [1][1], 5x5 -[2][2])
def main():
    n, m, matriz = getMatriz()

    getSoma(matriz, n, m)


def getMatriz():
    nstr, mstr = str(input()).split(" ")
    n = int(nstr)
    m = int(mstr)
    mat = []

    for i in range (n):
        linha = str(input()).split(" ")
        linhaInt = []
        for j in range (m):
            linhaInt.append(float(linha[j]))

        mat.append(linhaInt)

    return n, m, mat

def getSoma(matriz, n, m):
    soma = 0

    for i in range(n):
        if (i == 0 or i == n-1):
            for j in range (m):
                soma = soma + matriz[i][j]
        else:
            soma = soma + matriz[i][0] + matriz[i][m-1]
    
    print ("Borda = %.2f" % soma)#- elemento central
    
main()

#n=1, 3, 5, 7, 11, 13
