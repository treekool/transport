#!/usr/bin/env python2
import numpy as np

#m = 5
#n = 3

#a = [320,280,250]
#b = [150,140,110,230,220]

#c = [[20,25,20,15,24],
#     [29,15,16,19,29],
#     [6,11,10,9,8]]

#c = [[20,29,6],
#     [25,15,11],
#     [20,16,10],
#     [15,19,9],
#     [24,29,8]]

n = 4
m = 4

a = [14,20,26,41]
b = [30,22,15,34]

c = [[70,38,24,92],
     [58,18,56,72],
     [19,10,100,30],
     [3,36,121,8]]

a = [200,180,190,50]
b = [150,180,150,140]

c = [[7,8,1,2],
     [4,5,9,8],
     [9,2,3,6],
     [0,0,0,0]]

def findMinRow(n,k,arr,mzero,recurs):
    class ret:
        val = 0
        ind = 0
        
    tmp = 0
    for i in range(n):
        tmp = arr[k][i] + tmp
        
    lost = -1
    for r in range(recurs):
        ret.val = tmp
        l = 0
        for i in range(n):
            if(arr[k][i] == lost):
                l = l + 1
            if(l>1):
                lost = -1
        for i in range(n):
            if(ret.val > arr[k][i] and lost < arr[k][i] and mzero[k][i] !=1 ):
                ret.val = arr[k][i]
                ret.ind = i
                
        lost = ret.val
        
    return ret

def findMinColums(n,k,arr,mzero,recurs):
    class ret:
        val = 0
        ind = 0
    
    tmp = 0
    for i in range(n):
        tmp = arr[i][k] + tmp
        
    lost = -1
    for r in range(recurs):
        ret.val = tmp
        l = 0
        for i in range(n):
            if(arr[i][k] == lost):
                l = l + 1
            if(l>1):
                lost = -1
        for i in range(n):
            if(ret.val > arr[i][k] and lost < arr[i][k] and mzero[i][k] != 1):
                ret.val = arr[i][k]
                ret.ind = i
        lost = ret.val
        
    return ret

def findMax(n,arr):
    class ret:
        val = 0
        ind = 0
    
    ret.val = arr[0]
    for i in range(n):
        if(ret.val < arr[i]):
            ret.val = arr[i]
            ret.ind = i
    return ret

def findIndexsMinInMatrix(n,m,matrix,value):
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == value): return [i,j]

    return [-1,-1]

def outMatrix(n,m,a,b,matrix1,matrix2):
    for i in range(m):
        print 'c:\t',
        for j in range(n):
            print matrix1[i][j],"\t",
        print '|',a[i]
        print 'x:\t',
        for j in range(n):
            print matrix2[i][j],"\t",
        print '|'

    for j in range(n):
        print '---------',
        
    print '\nb:\t',
    for j in range(n):
        print b[j],"\t",
    print
    
    return 0

# for cal Y
def mulLists(n,m,a,b):
    ret = 0
    for i in range(m):
        for j in range(n):
            ret = a[i][j]*b[i][j] + ret
    return ret

def wrEl(row,colum,a,b,x):
    if a[row] < b[colum]:
        b[colum] = b[colum] - a[row]
        x[row][colum] = a[row]
        a[row] = 0
    else:
        a[row] = a[row] - b[colum]
        x[row][colum] = b[colum]
        b[colum] = 0
    return 0

# Fogel Method
def fogelMethod(n,m,a,b,c,x):
    da = np.zeros([m])                 # for Fogel method
    db = np.zeros([n])                 # different min values tarif

    mzero = np.zeros([m,n]);
    add_a_b = 1
    
    while add_a_b != 0:
    #for clk in range(10):
        row =  0
        colum = 0
        add_a_b = 0
        
        # min in row
        for i in range(m):
            da[i] = findMinRow(n,i,c,mzero,2).val - findMinRow(n,i,c,mzero,1).val
#        print da
    
        # min in colums
        for i in range(n):
            db[i] = findMinColums(m,i,c,mzero,2).val - findMinColums(m,i,c,mzero,1).val
#        print db
    
        max_row= findMax(m,da)
        max_colum = findMax(n,db)

        if max_row.val > max_colum.val:
            row = max_row.ind
            da[row] = -1
            colum = findMinRow(n,row,c,mzero,1).ind
            
            #print 'row',row           
            #print 'colum',colum
        else:
            colum = max_colum.ind
            db[colum] = -1
            row = findMinColums(m,colum,c,mzero,1).ind
        
            #print 'colum',colum
            #print 'row', row

        mzero[row][colum] = 1
        # writen in tarif array elemet
        wrEl(row,colum,a,b,x)
    
        for i in range(m):
            add_a_b = add_a_b + a[i]
        for j in range(n):
            add_a_b = add_a_b + b[i]

#        print "a+b:",add_a_b
    
    return 0

def setPotencial(n,m,c,x,u,v,s):

    slaveU = np.zeros([m])
    slaveV = np.zeros([n])

    slaveU[0] = 1

    while (1):
        slave = 1
        for i in range(m):
            slave = slave * slaveU[i]
        for j in range(n):
            slave = slave * slaveV[j]
    
        for i in range (m):
            for j in range (n):
                if(x[i][j]!=0):
                    if(slaveU[i] == 1):
                        v[j] = c[i][j] - u[i]
                        slaveV[j] = 1
                    if(slaveV[j] == 1):
                        u[i] = c[i][j] - v[j]
                        slaveU[i] = 1

        if(slave == 1): break

    for i in range (m):
        for j in range (n):
            if(x[i][j]==0): s[i][j] = c[i][j] - (u[i] + v[j]) 
            
    return 0

def testPotencialS(n,m,s):
    s_min = 0
    for i in range (n):
        for j in range (m):
            if(s[i][j] < 0):
                if(s[i][j] < s_min): s_min = s[i][j]
    return s_min


def moveTo(i0,j0,i1,j1,matrix,value):
    matrix[i1][j1] = matrix[i1][j1] + value;
    matrix[i0][j0] = matrix[i0][j0] - value;
    return 0

def findAngleX(i0,j0,m,matrix):
    angleX = [[i0,j0],[i0,j0]]
    j=j0-1
    while(j>0):
        if(matrix[i0][j]!=0):
            angleX[0] = [i0,j]
        else:
            break
        j = j - 1
        
    j=j0+1
    while(j<m):
        if(matrix[i0][j]!=0):
            angleX[1] = [i0,j]
        else:
            break
        j = j + 1
    return angleX

def findAngleY(i0,j0,n,matrix):
    angleY = [[i0,j0],[i0,j0]]
    i=i0-1
    while(i>0):
        if(matrix[i][j0]!=0):
            angleY[0] = [i,j0]
        else:
            break
        i = i - 1
        
    i=i0+1
    while(i<n):
        if(matrix[i][j0]!=0):
            angleY[1] = [i,j0]
        else:
            break
        i = i + 1
    return angleY

def main():
    # Tarifs #
    x = np.zeros([m,n])
    
    outMatrix(n,m,a,b,c,x)
    print "\nOverarching plan:"
    # !!! Overarching plan !!! #
    fogelMethod(n,m,a,b,c,x)
    outMatrix(n,m,a,b,c,x)
    Y = mulLists(n,m,x,c)
    print 'Y =', Y
    Y_old = Y + 1   # =)

    while (Y < Y_old):
        Y_old = mulLists(n,m,x,c)
    # !!! potencials !!! #
        u = np.zeros([m])
        v = np.zeros([n])
        s = np.zeros([n,m])
        
        setPotencial(n,m,c,x,u,v,s)
        #print 'U:',u
        #print 'V:',v
        #print 'S:',s
    
        min_s = testPotencialS(n,m,s)
        #print min_s
        m_index_s = findIndexsMinInMatrix(n,m,s,min_s)
        #print m_index_s
        
        cyrcle_X=findAngleX(m_index_s[0],m_index_s[1],m,x)
        #print cyrcle_X
        angles1 = findAngleY(cyrcle_X[0][0],cyrcle_X[0][1],n,x)
        angles2 = findAngleY(cyrcle_X[1][0],cyrcle_X[1][1],n,x)

        #print angles1
        #print angles2
    
        x_a = x[angles1[0][0]][angles1[0][1]]
        x_b = x[angles2[1][0]][angles2[1][1]]

        if(x_a >= x_b):
            min_x = x_b
        else:
            min_x = x_a
         
        moveTo(angles1[0][0],angles1[0][1],angles2[0][0],angles2[0][1],x,min_x)
        moveTo(angles2[1][0],angles2[1][1],angles1[1][0],angles1[1][1],x,min_x)

        #outMatrix(n,m,a,b,c,x)
        Y = mulLists(n,m,x,c)
        print 'Y =', Y

    outMatrix(n,m,a,b,c,x)
    return 0

main()
