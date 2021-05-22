#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:08:32 2021

@author: martin
"""
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

class Fractals:
    def __init__(self,largeur=600,longueur=500):
        self.largeur=largeur
        self.longueur=longueur
        self.maxi=80
        self.set=[]
        
        
    def CreateSetJ(self,Re,Im,CRe,CIm):
        z=complex(Re,Im)
        c=complex(CRe,CIm)
        compt=0
        while abs(z)<2 and compt<self.maxi :
            compt+=1
            z=z**(2)+c
        return compt
        
    def CreateSetM(self,Re,Im):
        c=complex(Re,Im)
        z=0
        compt=0
        while abs(z)<2 and compt<self.maxi :
            compt+=1
            z=z**(2)+c
        return compt
    
    def MandelbrotSet(self,Zoom=1,ZoomH=0,ZoomV=0):
        if Zoom<=0:
            raise ValueError("The zoom can't be less or equal to 0")
        else:
            for i in range(0,self.largeur):
                for a in range(0,self.longueur):
                    x=i/(self.largeur/2-50)
                    y=a/(self.longueur/2)
                    c=self.CreateSetM((x+ZoomH-1.8)/Zoom,(y+ZoomV-1)/Zoom)
                    self.set.append([x,y,c])
    
    def JuliaSet(self,Re,Im,Zoom=1,ZoomH=0,ZoomV=0):
        if Zoom<=0:
            raise ValueError("The zoom can't be less or equal to 0")
        else:
            for i in range(0,self.largeur):
                for a in range(0,self.longueur):
                    x=i/(self.largeur/2-50)
                    y=a/(self.longueur/2)
                    c=self.CreateSetJ((x+ZoomH)/Zoom,(y+ZoomV)/Zoom,Re,Im)
                    self.set.append([x,y,c])
    
    def show(self):
        im = Image.new('RGB', (self.largeur,self.longueur), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for i in range(len(self.set)):
            x=self.set[i][0]*(self.largeur/2-50)
            y=self.set[i][1]*(self.longueur/2)
            color=round(self.set[i][2]*(255/self.maxi))
            # Plot the point
            draw.point([x, y], (color,color,color))
        im.save('output.png', 'PNG')
        image=Image.open('output.png')
        image.show()
        
        
def Mandelbrot():
        f=Fractals()
        f.MandelbrotSet()
        f.show()