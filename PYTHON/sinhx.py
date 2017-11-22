# -*- coding: utf-8 -*-
from math import sinh
x = 1. * input ("ievadi argumentu")

y=sinh(x/2)
print "sinh(%.2f) = %.2f"%(x,y)

k=0
a=x/(1*2)
s= a
print "a0 = %.2f " %(a)


while k < 500:
	k=k+1
	a=a*x*x/(2*k*(2*k+1))
	s= s+ a
print " a%d = %6.2f S%d = %6.2f"%(k,a,k,s)

