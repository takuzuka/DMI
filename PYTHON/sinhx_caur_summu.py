# -*- coding: utf-8 -*-
from math import sinh


def sinussh(x):
	k=0
	a=x/(1*2)
	s= a
	print "izdruka no liet.f. a0 = %6.2f S0 = %6.2f" %(a,s)


	while k < 500:
		k=k+1
		R=x*x/(2*k*(2*k+1))
		a=a*R
		s= s+ a
		print "izdruka no liet. f.  a%d = %6.2f S%d = %6.2f"%(k,a,k,s)

	print "izdruka no liet.f. Beigas"

	return s

x = 1. * input ("ievadi argumentu")
y=sinh(x/2)
print "standarta sinh(%.2f) = %.2f"%(x,y)
yy =sinussh(x)
print type(yy)
print "mans sinh(%.2f) = %6.2f"%(x,yy)

print "     500"
print "     ---        2*k+1"
print "     \         x"
print "s(x)= |  ------------------  " 
print "     /    	    2*k+1 "
print "     ---  (2*k+1)!*2 "
print "     n=0"
