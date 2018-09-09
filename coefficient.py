# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:49:02 2016

@author: adityagupta
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:22:31 2016

@author: adityagupta
"""
import numpy as np
def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrixadd(A,B):
    Z = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        Z.append(row)
    return Z



def scalarmulti(c,A):
    Z=[]    
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(c*A[i][j])
        Z.append(row)
    return Z


def trace(A):
    sum=0    
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if(i==j):
                sum=sum+A[i][j]
    return sum


def LF(A):
    ri=[]
    ci=[]
    rb=[]
    B=[]
    for i in range(len(A)):
        ri=[]
        rb=[]
        for j in range(len(A)):
            if(i==j):
                ri.append(1)
                rb.append(0)
            else:
                ri.append(0)
                rb.append(0)
        ci.append(ri)
        B.append(rb)
    coeffi=[1.0]
    for j in range(len(A)):
        B=matrixadd(matrixmult(A,B),scalarmulti(coeffi[j],ci))
        a=(-1/float(j+1))*trace(matrixmult(A,B))
        coeffi.append(a)
    return coeffi

       
        

            
    
