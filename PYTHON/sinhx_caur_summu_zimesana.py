# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def sinussh(x):
	k=0
	a=x/2
	s= a
	while k < 500: 
		k+=1
		R =x*x/(2*k*(2*k+1)*4)
		a = a * R
		s = s + a	
	return s

x = np.arange(-7.5,7.5,0.1)
y = sinussh(x)
plt.plot(x, y)
plt.show()
