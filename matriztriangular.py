def main():
    matriz = getMatriz()
    getTriangular(matriz)



def getMatriz():
    n = int(input())
    mat = []

    for i in range (n):
        linha = str(input()).split(" ")
        linhaInt = []
        for j in range (len(linha)):
            linhaInt.append(float(linha[j]))

        mat.append(linhaInt)

    return mat

def getTriangular(matriz):
    if len(matriz[0])!=len(matriz):
        return False

    triangularSuperior = 1
    triangularInferior = 1
    diagonal = 1

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i<j and matriz[i][j]!=0:
                triangularSuperior = 0
            if i>j and matriz[i][j]!=0:
                triangularInferior = 0
    
    if (triangularSuperior == 1 and triangularInferior == 1):
        print("diagonal")
    elif(triangularInferior == 1):
        print("triangular inferior")
    elif(triangularSuperior == 1):
        print("triangular superior")
    else:
        print("nao triangular")
                
main()
