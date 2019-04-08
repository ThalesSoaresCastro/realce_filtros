import cv2
import numpy as np

def main():

    img = cv2.imread('lena512.jpg', 0)
    #img2 =

    cv2.imshow('original', img)
    cv2.imshow('Difusao de Erro_Livro', difusao_Erro(img))
    cv2.imshow('Difusao de Erro', difusao_erro_FS(img))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


################################################################################
#   difusao de erro de Floyd e Steinberg
def difusao_Erro(f):
    size = f.shape
    g = np.zeros((size[0],size[1]),dtype='uint8')
    auxiliar = f.copy()
    erro = 0
    for i in range(size[0]-1):
        for j in range(size[1]-1):
            if auxiliar[i][j] < 128:
                g[i][j] = 0 #branco...
            else:
                g[i][j] =  1#preto...

            erro = auxiliar[i][j] - g[i][j]*255


            auxiliar[i+1, j] = auxiliar[i+1, j]+ (erro*(7/16))
            auxiliar[i-1, j+1] = auxiliar[i-1, j+1] + (erro*(3/16))
            auxiliar[i, j+1] = auxiliar[i, j+1] + (erro*(5/16))
            auxiliar[i+1, j+1] = auxiliar[i+1, j+1] + (erro*(1/16))

    return auxiliar

def difusao_erro_FS(f):

    (M, N) = f.shape
    valorLimite = 128
    aux = f.copy()
    g = np.zeros((M, N))
    (M, N) = (M - 1, N - 1)
    erro = 0

    for linha in range(M):
        g[linha, 0] = 255 * int(aux[linha, 0] >= valorLimite)
        erro = - g[linha, 0] + aux[linha, 0]
        aux[linha, 1] = 0.4375 * erro + aux[linha, 1]
        aux[linha + 1, 1] = 0.0625 * erro + aux[linha + 1, 1]
        aux[linha + 1, 0] = 0.3125 * erro + aux[linha + 1, 0]

        for coluna in range(1, N):
            g[linha, coluna] = 255.0 * int(aux[linha, coluna] >= valorLimite)
            erro = - g[linha, coluna] + aux[linha, coluna]
            aux[linha, coluna + 1] = 0.4375 * erro + aux[linha, coluna + 1]
            aux[linha + 1, coluna + 1] = 0.0625 * erro + aux[linha + 1, coluna + 1]
            aux[linha + 1, coluna] = 0.3125 * erro + aux[linha + 1, coluna]
            aux[linha + 1, coluna - 1] = 0.1875 * erro + aux[linha + 1, coluna - 1]

        g[linha, N] = 255 * int(aux[linha, N] >= valorLimite)
        erro = - g[linha, N] + aux[linha, N]
        aux[linha + 1, N] = 0.3125 * erro + aux[linha + 1, N]
        aux[linha + 1, N - 1] = 0.1875 * erro + aux[linha + 1, N - 1]

    g[linha, 0] = 255 * int(aux[linha, 0] >= valorLimite)
    erro = - g[linha, 0] + aux[linha, 0]
    aux[linha, 1] = 0.4375 * erro + aux[linha, 1]

    for coluna in range(1, N):
        g[linha, coluna] = 255 * (aux[linha, coluna] >= valorLimite)
        erro = - g[linha, coluna] + aux[linha, coluna]
        aux[linha, coluna + 1] = 0.4375 * erro + aux[linha, coluna + 1]

    g[linha, N] = 255 * (aux[linha, N] >= valorLimite)
    
    return g


################################################################################
if __name__ == '__main__':
    main()
