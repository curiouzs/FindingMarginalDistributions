import math
import numpy as np
pdf=[[0,0.01,0.03,0.05,0.07,0.09],[0.01,0.02,0.04,0.05,0.06,0.08],[0.01,0.03,0.05,0.05,0.05,0.06],[0.01,0.02,0.04,0.06,0.06,0.05]]

p_x=np.sum(pdf,axis=0)
p_y=np.sum(pdf,axis=1)

x=[0,1,2,3,4,5]
y=[0,1,2,3]
E_x=np.inner(x,p_x)
E_y=np.inner(y,p_y)

E_x_2=np.inner(np.square(x),p_x)
E_y_2=np.inner(np.square(y),p_y)

variance_x=E_x_2-E_x**2
variance_y=E_y_2-E_y**2
sd_x=math.sqrt(variance_x)
sd_y=math.sqrt(variance_y)

E_x_y=0
for i in range(4):
    for j in range(6):
        E_x_y=E_x_y+x[j]*y[i]*pdf[i][j]
        
Covariance=E_x_y-(E_x*E_y)
Covariance_coeff=Covariance/(sd_x*sd_y)

import pandas as pd
pdf_df=pd.DataFrame(pdf)
display(pdf_df)
print("Variance of X:\t\t\t\t",variance_x)
print("Variance of Y:\t\t\t\t",variance_y)
print("Standard deviation of X:\t\t",sd_x)
print("Standard deviation of Y:\t\t",sd_y)
print("Covariance:\t\t\t\t",Covariance.round(4))
print("Covariance Coefficient of Corelation:\t",Covariance_coeff.round(4))
