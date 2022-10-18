# -*- coding: utf-8 -*-
"""
Author: Nishant Yadav
ID: 19CY20025
Date: 12/10/2022
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def LJ(sig, eps, r):
    return 4*eps*((sig/r)**12 - (sig/r)**6)

r_min = 3
r_max = 15

x = np.linspace(r_min, r_max, 100, True)

y = LJ(3.4, 1, x)

plt.plot(x, y)
plt.xlabel("r/sigma")
plt.ylabel("Vlj/eps")
plt.show()