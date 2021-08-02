

#n é sempre ímpar, então há uma posição central de cada matriz (3x3 - [1][1], 5x5 -[2][2])
def main():
    n, m, matriz, vetor = getMatrizVetor()

    getProduto(matriz, vetor, n, m)


def getMatrizVetor():
    nstr, mstr = str(input()).split(" ")
    n = int(nstr)
    m = int(mstr)
    mat = []

    for i in range (n+1):
        linha = str(input()).split(" ")
        linhaInt = []
        for j in range (len(linha)):
            linhaInt.append(float(linha[j]))

        if (i < n):
            mat.append(linhaInt)
        else:
            vetor = linhaInt


    return n, m, mat, vetor

def getProduto(matriz, vetor, n, m):
    produto = []

    if len(vetor) != m:
        print("nao eh possivel fazer a operacao")
    else:
        for i in range(n):
            somaProduto = 0
            for j in range (m):
                    somaProduto = somaProduto + vetor[j] * matriz[i][j]
            produto.append(somaProduto)
            print(somaProduto)
    
main()
