import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d1=pd.read_csv(r"C:\Users\mayank\Desktop\test1.csv")
X=d1['x'].values
Y=d1['y'].values
plt.plot(X,Y)
plt.scatter(X,Y)

m_x=X.mean()
m_y=Y.mean()
sum_nr=0
sum_dr=0
for i in range (0,len(X)):
    
    nr=(X[i]-m_x)*(Y[i]-m_y)
    sum_nr=sum_nr+nr
    dr=(X[i]-m_x)**2
    sum_dr=sum_dr+dr
    
M=sum_nr/sum_dr
print(M)
c=m_y-(m_x*M)
print(c)

for i in range (0,len(X)):
    for i in range(0,len(Y)):
        
        Yp=(M*X+c) 
print(Yp)
plt.scatter(X,Y)
plt.plot(X,Yp)
plt.show()
error=[]
sum1=0
for i in range (0,len(X)):
    E=(Y[i]-m_y)**2
    sum1=sum1+E
    
print(np.sqrt(sum1))
m_yp=Yp.mean()
error_p=[]
sum2=0
for i in range (0,len(X)):
    E=(Yp[i]-m_yp)**2
    sum2=sum2+E
    
print(np.sqrt(sum2))
print(sum2/sum1)
