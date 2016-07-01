#sample_matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
#square_matrix = [[a1,a2,..an],[b1,b2,..bn],[c1,c2,..cn].....[n1,n2...nn]]
#matlab_mat= 1 2 3 4;5 6 7 8;9 10 11 12

def row(matrix,x):
    row=[]
    for i in range(len(matrix)):
        row.append(matrix[x-1][i])
    return row

def col(matrix,x):
    col=[]
    for i in range(len(matrix)):
        col.append(matrix[i][x-1])
    return col

def transpose(matrix):
    output=[]
    for i in range(len(matrix[0])): 
        row_=[]
        for j in range(len(matrix)):
            row_.append(matrix[j][i])
        output.append(row_)
    return output

def _2x2_(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

def CrossProduct(r1,r2):
    if len(r1)==len(r2):
        if len(r1)==3:
            i=r1[1]*r2[2]-r1[2]*r2[1]
            j=-(r1[0]*r2[2]-r1[2]*r2[0])
            k=r1[0]*r2[1]-r1[1]*r2[0]
            return [i,j,k]
        else:
            print "Hey! 3D vector please."
    else:
        print "What the hell is that?! Are you serious?"

def multiplication(m1,m2):
    if len(m1[0])==len(m2):
        row=len(m1)
        col=len(m2[0])
        output=[]
        s=0
        for i in range(row):
            output.append([])
            for j in range(col):
                for a in range(len(m1[0])):
                    s=s+m1[i][a]*m2[a][j]
                output[i].append(s)
                s=0
        return output
    else:
        print "Invalid input!"
        
def sgn(i,j):
    if (i+3)%2==1:
        if (j+3)%2==1:
            return 1
        else:
            return -1
    else:
        if (j+3)%2==1:
            return -1
        else:
            return 1

def subMat(matrix,i,j):
    output=[]
    cout=0
    for x in range(len(matrix)):
        if x!=i:
            output.append([])
            for y in range(len(matrix[0])):
                if y!=j:
                    output[x-cout].append(matrix[x][y])       
        else:
            cout+=1
    return output
        
def det(matrix):
    if len(matrix)==len(matrix[0]):
        if len(matrix)==2:
            return _2x2_(matrix)
        else:
            output=0
            for i in range(len(matrix)):
                output+=matrix[i][0]*sgn(i,0)*det(subMat(matrix,i,0))
            return output
    else:
        print "Please input a square matrix"

def format_conv(matlab_mat):
    raw_mat=matlab_mat.split(";")
    output=[]
    for i in range(len(raw_mat)):
        raw_row=raw_mat[i].split()
        output.append([])
        for j in raw_row:
            output[i].append(float(j))
    return output


#A=format_conv(open("data0.txt").read())
#5x5
#B=format_conv(open("data1.txt").read())
#6x6
#C=format_conv(open("data2.txt").read())
#7x7
#D=format_conv(open("data3.txt").read())
#8x8
#E=format_conv(open("data4.txt").read())
#9x9
#F=format_conv(open("data5.txt").read())
#10x10
#G=format_conv(open("data6.txt").read())
#11x11

#import time
#t0=time.time()
#det(A)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(B)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(C)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(D)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(E)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(F)
#t1=time.time()
#print t1-t0,
#t0=time.time()
#det(G)
#t1=time.time()
#print t1-t0,
