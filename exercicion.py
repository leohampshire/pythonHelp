#n é sempre ímpar, então há uma posição central de cada matriz (3x3 - [1][1], 5x5 -[2][2])
def main():
    matriz = getMatriz()
    print ("X =",soma_diagonal1(matriz) + soma_diagonal2(matriz)) #- elemento central
    


def getMatriz():
    n = int(input())
    mat = []

    for i in range (n):
        linha = str(input()).split(" ")
        linhaInt = []
        for j in range (len(linha)):
            linhaInt.append(int(linha[j]))

        mat.append(linhaInt)

    return mat

def soma_diagonal1(matriz):
    soma = 0 
    N= min(len(matriz), len(matriz[0]))
    for i in range (0,N):
        soma = soma + matriz[i][i]
    return soma
    
def soma_diagonal2(matriz):
    soma = 0
    M = min(len(matriz), len(matriz[0]))
    for i in range (0,M):
        soma = soma + matriz[i][M-i-1] 
    return soma
    
main()

#n=1, 3, 5, 7, 11, 13
