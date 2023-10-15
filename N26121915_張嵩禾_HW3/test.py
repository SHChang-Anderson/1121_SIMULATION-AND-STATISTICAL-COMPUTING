import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

p = 0.2  # 成功的概率
x = np.arange(1, 21)  # 試驗次數範圍


pmf = geom.pmf(x, p)
print(pmf)

plt.bar(x, pmf)
plt.xlabel('Number of Trials')
plt.ylabel('Probability')
plt.title(f'Geometric Distribution (p = {p})')
plt.show()
