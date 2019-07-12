import matplotlib.pyplot as pl

z = [[-3,2],[0,-1],[0,3],[1,2],[3,-3],[3,5],[3,5]]
z1 = [i[0] for i in z]
z2 = [k[1] for k in z] 
y = [-1,-1,-1,1,1,1,1]



w = [-1, 0]
wt = np.transpose(w)
for i in range(len(z)):
	left = np.matmul(wt, z[i])
	print(left)