import random
import matplotlib.pyplot as plt
import math
from scipy import integrate

sum = 0
ct = 0
ctt = 0
lambda1 = 2.5
simtuT = input("Please Enter the simlulate times : ") 
simtuT = int(simtuT)
for i in range(simtuT):
    sum = 1
    ct = 0
    varr = 0
    while(1):
        varr = random.uniform(0,1)
        sum *= varr
        ct += 1
        if(sum < math.exp(-lambda1)):
            break
    ct = ct - 1
    ctt += ct

print(ctt/simtuT)
