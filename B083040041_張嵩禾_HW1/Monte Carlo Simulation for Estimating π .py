import matplotlib.pyplot as plt
import numpy as np

def Q(x_s): 
    E_s = 106.2e-14
    lambda_i = 0.00238382
    kT = 0.0259
    q = 1  # eV
    u_b = 12
    u_s = q/kT * x_s + u_b

    Q = E_s/lambda_i * (kT / q) * np.sqrt(2) * np.sqrt((u_b - u_s)*np.sinh(u_b)-(np.cosh(u_b) - np.cosh(u_s)))

    return 0.3+Q/0.69e-7
def Q1(x1):
    return x1
"""
x = []
y = []
x1 = []
y1 = []
fin_b = 0.311
for i in np.arange(-(0.56-np.abs(fin_b)), 0.56+np.abs(fin_b), 0.01):
    x.append(i)
    y.append(Q(i))
minm = 99999
ans = 0
for i in np.arange(-(0.56-np.abs(fin_b)), 0.56+np.abs(fin_b), 0.01):
    if(abs(Q(i) - i) < minm):
        ans = i
#plt.ylim(1e-10,1e-8)
print(i)
plt.plot(x, y, color='green', marker='o', linestyle='dashed')
plt.plot(x1, y1, color='red', marker='o', linestyle='dashed')
plt.show()
"""""