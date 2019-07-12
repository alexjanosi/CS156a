from sklearn import svm

x = [[1,0],[0,1],[0,-1],[-1,0],[0,2],[0,-2],[-2,0]]
y = [-1,-1,-1,1,1,1,1]

clf = svm.SVC(kernel='poly',C=float("inf"), degree=2, gamma=1,coef0=1)
clf.fit(x,y)
print(len(clf.support_))