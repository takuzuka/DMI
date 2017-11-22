# -*- coding: utf-8 -*-
from math import sinh, e

x = 1 * input ("ievadi argumentu")

y= sinh(x/2)
print "sinh(x/2)(%.2f) = %.2f"%(x,y)

s=(e**(x/2)-e**(-x/2))/2
print "sinh(x/2)(%.2f) = %.2f"%(x,s)


y=sinh(x)
print "sinh (%.2f) = %.2f"%(x,y)

k=(e**x-e**(-x))/2
print "sing (%.2f) = %.2f"%(x,k)
