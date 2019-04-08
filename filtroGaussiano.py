import cv2
import numpy as np

def main():
    img = cv2.imread('lena512.jpg',0)


   # print(triangulo_Pascal(5))
    cv2.imshow('original', img)
    cv2.imshow('resultado',filtro_gaussiano(img, 5))

    filtro_cv2 = cv2.GaussianBlur(img,(5,5),0)

    cv2.imshow('filtro_CV2', filtro_cv2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

###########################################################

#       Funcoes

#tratar as bordas...
def filtro_gaussiano(imagem, tamanho):

    size = imagem.shape
    g_inicial = np.zeros((size[0], size[1]), dtype = 'uint8')
    g_final = np.zeros((size[0], size[1]), dtype = 'uint8')

    fator = (np.power(2,(tamanho-1)))

    mask = (triangulo_Pascal(tamanho))/fator

    for i in range(size[0]-tamanho//2):
        for j in range(size[1]-tamanho//2):
            soma = 0
            for u in range(tamanho):
                    if j>=tamanho//2:
                     soma = soma + imagem[i,j-(tamanho//2)+u]*mask[u]
            g_inicial[i,j] = soma

    for i in range(size[0]-tamanho//2):
        for j in range(size[1]-tamanho//2):
            soma = 0
            for u in range(tamanho):
                    if i>=tamanho//2 :
                        soma = soma + g_inicial[i-(tamanho//2)+u, j]*mask[u]
            g_final[i,j] = soma

    return g_final


def triangulo_Pascal(n):
    lista = [1]
    lista_aux = lista
    for i in range(2,n+1):
        lista = [1,1]
        n_aux = len(lista_aux)
        for j in range(1,n_aux):
            lista.insert(j,lista_aux[j]+lista_aux[j-1])
        lista_aux = lista;
    return lista

if __name__ == '__main__':
    main()
