def bruteforce():
        from newtonmethod import newton as nt
        from coefficient import LF
        def f(a,x):
            sums=0
            for i in range(0,len(x)):
                z=x[i]*(a**(len(x)-(i+1)))
                sums=sums+z
            return sums
            
            
            
            
        def derivative(x):
            a=[]
            for i in range(len(x)-1):
                p=(len(x)-(i+1))*x[i]
                a.append(p)
            
            return a
        
        
        def falseposition(coeff,a,b):
            a1=f(a,coeff)
            b1=f(b,coeff)
            if(a1*b1<0):
                p=0    
                while(p==0):
                    if(a1<0 and b1>0):
                        c=(a*b1-b*a1)/float(b1-a1)    
                    elif(b1<0 and a1>0):
                        c=(b*a1-a*b1)/float(a1-b1)
                    c1=f(c,coeff)
                    if(c1<=0.0000001 and c1>=0):
                        print c
                        break
                    elif(c1*a1<0):
                        b=c
                    elif(c1*b1<0):
                        a=c
        
        
        
        
        diff=0.0000001                
        def secant(co,a,b):
            if len(co) > 2:
             if len(co)%2 == 0:
              while abs(a-b) > diff:
               new  = a - (f(a,co)*(b-a))/float(f(b,co)-f(a,co))
               a = b
               b = new
               #print a,b
              return a
              
             else:
                 b = (a+b)/2#meathod doesnt work or even orderd poly so this is added.
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
        
        
        def bisection(coeff,a,b):
            a1=f(float(a),coeff)
            b1=f(float(b),coeff)
            if(a1*b1<0):
                p=0    
                while(p==0):
                    c=(a+b)/2.0
                    c1=f(float(c),coeff)
                    if(c1<=0.00000001 and c1>=0):
                        
                        return c
                        break
                    elif(c1*a1<0):
                        b=c
                    elif(c1*b1<0):
                        a=c
                        
                        
        def euclidian(x,y):
            i=0
            
            y1=[1]
            while i<len(y)-2:
                
                d=y1[i]/x[0]
                c=y[i+1]-(d*x[1])
                y1.append(c)
                
                i=i+1
            
            return y1
            
            
            
        def limits(pol):
         
            import math
            n = len(pol) - 1
            if len(pol) >= 3:    
                p1 = ((-1)*pol[1])/float(n*pol[0])
                p2 = (n-1)/float(n*pol[0])
                sr = pol[1]**2 - (2*n*pol[0]*pol[2])/float(n-1)
                root = math.sqrt(sr)   
                u_b = p1 + p2*root
                l_b = p1 - p2*root
                aa= int(u_b+1)#upper bound
                bb = int(l_b-1)#lower bound
            return float(aa),float(bb)
        
        
        
        
        def evenlimits(pol):
                aa,bb=limits(pol)
                if(aa<bb):
                    while(aa<bb):
                        if(f(aa,pol)*f(bb,pol)<=0.0001):
                            return aa,bb
                        else:
                            aa=aa+0.01
                else:
                    while(aa>bb):
                        if(f(aa,pol)*f(bb,pol)<=0.00001):
                            return aa,bb
                        else:
                            bb=bb+0.01
            
                
            
                    
                
        
        def final(pol):
            import math
            
            roots=[]
            lm=0
            if(len(pol)>3):
                while lm==0:        
                    if(len(pol)>3):
                        if len(pol)%2==0:
                            aa,bb=limits(pol)
                        elif len(pol)%2!=0:
                            
                            aa,bb=evenlimits(pol)
                        
                        #x1=secant(pol,aa,bb)
                        x1=bisection(pol,aa,bb)
                        #x1=nt(pol)
                        roots.append(x1)
                        
                        
                        pol=euclidian([1,-x1],pol)
                        if(len(roots)==len(coef)-3):
                            break
            if(len(pol)==3):
                x2=(-pol[1]+ math.sqrt((pol[1]**2)-4*pol[0]*pol[2]))/2.0
                x3=(-pol[1]- math.sqrt((pol[1]**2)-4*pol[0]*pol[2]))/2.0
                roots.append(x2)
                roots.append(x3)
                
                
            
            
            
                    
            
            return roots
        def matrix():
            order = input('Enter the order of the matrix:')
            matrix =[]
            for row in range(order):
                matrix.append([])
                for column in range(order):
                    print 'enter the ',row+1,'*',column+1,'element '
                    inp = input ('-  ')
                    matrix[row].append(inp)
            return matrix
        a=matrix()
        coef = LF(a)
        print coef
        #coef = [1,3760,1979253,225138302,-16758029992,311469086688,-1747559233152,3019567887360]
        #coef=[1,16,20,-112]
        #coef=[1,4,-4,-16]
        #coef=[1,-17,58,316,-1592,-992,5376]
        #coef=[1,-4,4]
        x=final(coef)
        print ""
        print "The eigenvalues are: "
        print ""
        print x
bruteforce()
                                
        
        
        
        
        
        
        
            
                        
            