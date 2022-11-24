import numpy as np
import random

#(a)
n = 4
mat=[[0]*n]*n
mat=np.array(mat)

for i in range(0, n):
    for j in range(0, n):

        if i==0 and j==0:
            mat[i, j]=random.randint(1, 100)
            continue
        if i!=0 and j==0:
            if mat[i-1, j]%2==0:
                num=random.randint(1, 100)
                while(num%2!=0):
                    num=random.randint(1, 100)
                mat[i, j]=num
        
            elif mat[i-1, j]%2!=0:
                num=random.randint(1, 100)
                while(num%2==0):
                    num=random.randint(1, 100)
                mat[i, j]=num
            continue
        if mat[i, j-1]%2==0:
            num=random.randint(1, 100)
            while(num%2!=0):
                num=random.randint(1, 100)
            mat[i, j]=num
        
        elif mat[i, j-1]%2!=0:
            num=random.randint(1, 100)
            while(num%2==0):
                num=random.randint(1, 100)
            mat[i, j]=num
print("(a)")
print(mat)

#(b)
def printCommonElements(mat):

	mp = dict()
	for j in range(n):
		mp[mat[0,j]] = 1

	for i in range(1, n):
		for j in range(n):
	
			if (mat[i,j] in mp.keys() and [mat[i,j]] == i):
				mp[mat[i,j]] = i + 1

				if i == n - 1:
					print(mat[i,j], end = " ")
print("(b)")
printCommonElements(mat)
print()

#(c)
def shiftMatrixByK(mat, k):
	if (k > n) :
		print ("shifting is"
			" not possible")
		return
	
	j = 0
	while (j < n) :
		for i in range(k, n):
			print ("{} " .
			format(mat[j,i]), end="")
			
		for i in range(0, k):
			print ("{} " .
			format(mat[j,i]), end="")
			
		print ("")
		j = j + 1
print("(c)")
shiftMatrixByK(mat, 1)
print()
