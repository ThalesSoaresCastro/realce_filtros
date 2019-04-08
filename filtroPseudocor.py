# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:39:20 2018

@author: Typhanael
"""
import cv2
import numpy as np


def main():
     img = cv2.imread('flor.jpg', 0)


     cv2.imshow('original', img)
     cv2.imshow('imagem', pseudoCor(img))

     cv2.waitKey(0)
     cv2.destroyAllWindows()

###############################################################################
#       funcoes...
def pseudoCor(f):
    size = f.shape

    g = np.zeros((size[0],size[1], 3), dtype = 'uint8' )

    for i in range(size[0]):
        for j in range(size[1]):
            if(f[i][j] >=0 and f[i][j]<32):
                g[i][j] = [255,0,0]
            elif(f[i][j]>=32 and f[i][j]<64):
                g[i][j] = [0,0,255]
            elif(f[i][j]>=64 and f[i][j]<96):
                g[i][j] = [0,255,0]
            elif(f[i][j]>=96 and f[i][j]<128):
                g[i][j] = [255,255,0]
            elif(f[i][j]>=128 and f[i][j]<160):
                g[i][j] = [255,0,255]
            elif(f[i][j]>=160 and f[i][j]<192):
                g[i][j] = [255,0,255]
            elif(f[i][j]>=192 and f[i][j]<224):
                g[i][j] = [255,126,0]
            elif(f[i][j]>=224):
                g[i][j] = [255,0,126]

    return g

if __name__ == "__main__":
    main()
