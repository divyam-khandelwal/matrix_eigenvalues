#from bruteforce import bruteforce as br

def f(x,coef):
    #print coef
    ex = len(coef)#highest exponent power
    fun = 0
    for i in range(ex):
        ini = 1
        for m in range(i):#the first time i==0 so x is multiplied 0 times and so on..
            ini *= x #the number of times  x is multiplied and then multipliedwith the coefficient
        fun += ini*coef[ex-1-i]#the elements are added from the backside of the list
    return fun
#print f(3,coef)
#roots=[]
#pol = coef
#laguerre-samuelson inequality props of polynomials wikki
def limits(pol):
 import math
 n = len(pol) - 1
 if len(pol) >= 3:
  try:  
   p1 = ((-1)*pol[1])/float(n*pol[0])
   p2 = (n-1)/float(n*pol[0])
   sr = pol[1]**2 - (2*n*pol[0]*pol[2])/float(n-1)
   root = math.sqrt(sr)   
   u_b = p1 + p2*root
   l_b = p1 - p2*root
   aa= int(u_b+1)#upper bound
   bb = int(l_b-1)#lower bound
  except:
      aa1 = 'img'
      bb1 = 'img'
      return aa1, bb1
 else :
     aa = None
     bb = None
 return aa,bb
    #print 'root is ',pol[1]/pol[0]
 #n = len(coef)
 #print aa,bb
diff = 0.000000001
def secant(f,co,a,b):
    if len(co) > 2:
     if len(co)%2 == 0:
      while abs(a-b) > diff:
       new  = a - (f(a,co)*(b-a))/float(f(b,co)-f(a,co))
       a = b
       b = new
       #print a,b
      return a
      
     else:
         b = (a+b)/2.0
         while abs(a-b) > diff:
          try: 
           new  = a - (f(a,co)*(b-a))/float(f(b,co)-f(a,co))
           a = b
           b = new
           #print a,b
          except:
              return None
         return a
         
    else:
        if len(co) ==2:
          try:
            return (-1)*co[1]/co[0]
          except:
              return 0
        elif co[0] != 0 :
            return 'No real number'
        else:
            return 'Every real number '
#print secant(f,aa,bb),'is a root with secant meathod.'
def bisection(f,co,a,b):
    
    if len(co) > 2:
     c = (a+b)/2.0
     
     while abs((a-b)/2.0) > diff:
        # print co,f(a,co),f(c,co)
         if f(c,co) == 0:
             return c
         elif (f(a,co))*(f(c,co)) < 0:
             b = c
             
         else:
             a = c
         c = (a+b)/2.0
        
     return c
    else: 
        if len(co) ==2:
         try:   
          return (-1)*co[1]/co[0] 
         except:
             return 0
        elif co[0] != 0 :
            return 'No real number'
        else:
            return 'Every real number'
#print bisection(f,co,aa,bb),'is a root with bisection meathod.'
#ro1 = bisection (f,coef,aa,bb)
def symdiv(cof,a):
    out = []
    out.append(cof[0])
    t = True
    ct = 0
    val = cof[0]
    while t:
        ct+=1
        val*= a
        val += cof[ct]
        out.append(val)
        if ct == len(cof) - 1:
            t = False
    return out
#print symdiv(coef,3)
#to get all the roots using bisection meathod
def allroots(f,coef,aa,bb):
  orde = len(coef) - 1
  n = 0
  roots = []
  cnt = 0
  while n < orde:
      #print coef
      ro = secant(f,coef,aa,bb)
      if ro != None:
        cnt+=1
          
        roots.append(ro)
      else:
          if cnt != 0:
            roots.append('Other roots are imginary')
          else:
              roots.append('All roots are imaginary')
          break
     # print ro,n
      coef = symdiv(coef,ro)
      #print coef
      coef.pop()
      #print coef
      n+=1
  return roots
#print allroots(f,coef,aa,bb),'all roots'
def derivative (k):
    ot = []
    ii = len(k)
    for i in k[:len(k)-1]:
        ii-=1
        new = i*ii
        ot.append(new)
    return ot
order = input('Enter the order of the matrix:')
matrix =[]
for row in range(order):
    matrix.append([])
    for column in range(order):
        print 'enter the ',row+1,'*',column+1,'element '
        inp = input ('-   ')
        matrix[row].append(inp)
import numpy
coef = numpy.poly(matrix)    
#coef = [1,3760,1979253,225138302,-16758029992,311469086688,-1747559233152,3019567887360]
#coef = [1,1,1]
#coef = [1,0,0,1]
tco = tuple(coef)
#print derivative(coef)
print 'Do you want to enter the bounds to the roots of the function?'
print ""
choose  = raw_input('Y/N - ')
try:
 if choose == 'N'  :
  if len(coef) %2 == 0:
   aa = limits(coef)[0]  
   bb = limits(coef)[1]
  else:
      aa = limits(coef)[0]
      newc = derivative(coef)
      droots = allroots(f,newc,limits(newc)[0],limits(newc)[1])
      for i in droots:
          ltc = list(tco)
          if f(i,tco) * f(aa,coef) < 0:
              bb = i
              break
          bb = limits(coef)[1]
 else:
     k1 = True
     k2 = True
     while k1 and k2:
      aan = input('Enter the value of the lower bound to the roots:')
      bbn = input ('Enter the value to the upper bounds to the roots:')
      aa = limits(coef)[0]  
      bb = limits(coef)[1]
      if aan < aa:
          print 'Lower limit does\'nt bind all the roots'
         # bo1 = raw_input('Do you eant to continue (Y/N) :')
          #if bo1 == 'N':
          k1 = True
      else:
          k1 =False
     if bbn > bb:
          print 'Upper limit does\'nt bind all the roots'
          # bo2 = raw_input('Do you eant to continue (Y/N) :')
          #if bo2 == 'N':
          k2 = True
     else:
          k2 = False
 print ""
 print "The eigenvalues are:" 
 print ""
 print allroots(f,coef,aa,bb)
 print ""
 print bisection(f,coef,aa,bb),'is a root with bisection method.'
 print ""    
 print secant(f,coef,aa,bb),'is a root with secant method.'
except:
    print "All roots are imaginary "
    
#bruteforce() 



        
    
        
        
        
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    