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
b=7.0001
x = np.arange(a,b,0.1)
y = sinussh(x)
plt.plot(x,y)
#plt.show()

delta_x = 1.e-3
funa = sinussh(a)
funb = sinussh(b)
if funa * funb >0:
        print "[%.2f, %.2f] intervala saknu nav"%(a,b)
        print "vai saja intervala ir paru saknu skaits"
        exit()
print "turpinajums, kad sakne ir"
print "vertibas intervala galapunktos - "
print "f(%.2f)=%.2f un f(%.2f)=%.2f"%(a,funa,b,funb)


k=0
while b-a > delta_x:
        k += 1
        x = (a+b)/2
        funx = sinussh(x)
        print "%3d. a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
        if funa * funx > 0:
                a=x
        else:
                b=x
print "rezultats:"
print "a=%.9f f(%.9f)=%12.9f b=%.9f"%(a,x,funx,b)
print "aprekins veikts ar %d iteracijam"%(k)
