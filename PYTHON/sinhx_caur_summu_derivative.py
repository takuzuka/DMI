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

a=-7.5
b=7.5
x = np.arange(a,b,0.005)
y = sinussh(x)
plt.plot(x, y)
#plt.show()

n= len(x)
y_prim = []
for i in range(n-1):
        #print i,x[i], y[i]
        delta_y = y[i+1] - y[i]
        delta_x = x[i+1] - x[i]
        #y_prim = delta_y/delta_X
        #print y_prim
        y_prim.append(delta_y/delta_x)
plt.plot(x[:n-1],y_prim)


y_primprim = []
for i in range(n-2):
        delta_y_prim = y_prim[i+1] - y_prim[i]
        y_primprim.append(delta_y_prim/delta_x)
plt.plot(x[:n-2],y_primprim)

plt.show()
