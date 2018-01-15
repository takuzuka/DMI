# -*- coding: utf-8 -*-
from math import sinh


def sinussh(x):
	k=0
	a=x/2
	s= a
	while k < 500: 
		k+=1
		R =x*x/(2*k*(2*k+1)*4)
		a = a * R
		s = s + a
		if k == 499:
			print "a499 = %6.2f S499= %6.2f"%(a,s)

	print "izdruka no liet.f. Beigas"

	return s

x = 1. * input ("ievadi argumentu")
y=sinh(x/2)
print "standarta sinh(%.2f) = %.2f"%(x,y)
yy =sinussh(x)
print type(yy)
print "mans sinh(%.2f) = %6.2f"%(x,yy)

print "     500	"
print "     ---        2*k+1	                   2	"
print "     \         x                          x "
print "s(x)= |  ------------------  	R=----------------- " 
print "     /    	    2*k+1 	                 2 "
print "     ---  (2*k+1)!*2                2*k*(2*k+1)*2"
print "     n=0				"


