# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:07:19 2016

@author: Revathi Prasad
"""  
    
    
        
    
def func(x,co_eff):
    f=0
    ex=len(co_eff)
    for i in range(0,ex):
        m=co_eff[ex-i-1]
            #print x
        s=float(x**i)
        f=f+(m*s)
    return f
        
def f1(x,co_eff):
    g = 0
    ex=len(co_eff)
    for i in range(1,ex):
        t=i*x**(i-1)
        g=g+(co_eff[ex-i-1]*t)
    return g
        
def newton(x0,co):
        epsilon=0.0000001
        x = x0
        error = 100
        while error>epsilon:
            old = x        
            x = old-(float(func(x,co))/f1(x,co))
            error = abs(old-x)
        return x
        
def get_bolzanos(coeffs):
        neg = -1000
        posi = 1000
        a = 0
        b = 0
        for i in range(-1000,1000):
            val = func(i,coeffs)
            if val>0 and val<posi:
                b = i
                posi = val
                continue
            if val<0 and val>neg:
                a = i
                neg = val
                continue
        return (a,b)
        
    
coeffs=[1,3,2]
x0 =get_bolzanos(coeffs)[0]
p =newton(x0,coeffs)
print p
    