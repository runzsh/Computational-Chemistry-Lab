# -*- coding: utf-8 -*-
"""simpsonsMethod.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mYq5EYXDsjGW4PF4L9vOJZmXkCmRZWa7

```
File Name: Computational Chemistry Assignment 1
Created by: Nishant Yadav (19CY20025)
Date: 11/08/2022
```



**Simpson's Method for Numerical Integration:**

Method is based on approximating the subintervals using a quadratic curve. It only works with even number of subintervals.

`Applying Simpson's Method to approximate integral of sin(x) over a = 0 to b = pi`
"""

import numpy as np
import math

# Defining limits and interval size
a = 0
b = np.pi

#Total number of subintervals, need to be even for Simpson's Method
N = 10000                

# width of each subinterval, h
h = (b - a) /N

#Creating an array containing n + 1 points distributed uniformly, separated by 'h'
x = np.linspace(a, b, N + 1)

#I is storing the analytical value of integral for error calculation
I = 2                                       



# Defining the function to be integrated using Taylor Series
def f(x):
    ans = 0
    t = 10
    for i in range(t):
        ans = ans + ((((-1)**i)*(x**((2*i)+1)))/(math.factorial((2*i)+1)))
    return ans

# Calculating the function
areaSimp = (h/3) * (f(x[0]) + 2*sum(f(x[ : N-2 : 2])) + 4*sum(f(x[1 : N-1 : 2])) + f(x[N]))

# Absolute Error
absError = abs(I - areaSimp)

# Percentage Relative Error
PRE = absError*100/I



print("Numerical Value: ", areaSimp)
print("Absolute Error: ", absError)
print("Percentage Relative Error: ", PRE)

"""`Applying Simpson's Method to approximate integral of exp(x) over a = 0 to b = 1`"""

import numpy as np
import math

# Defining limits and interval size

a = 0
b = 1
N = 10000
h = (b - a) /N
x = np.linspace(a, b, N + 1)
I = np.exp(1) - 1

# Defining the function to be integrated using Taylor Series

def f(x):
    ans = 0
    t = 10
    for i in range(t):
        ans = ans + (x**i)/math.factorial(i)
    return ans

# Calculating the function

areaSimp = (h/3) * (f(x[0]) + 2*sum(f(x[ : N-2 : 2])) + 4*sum(f(x[1 : N-1 : 2])) + f(x[N]))

absError = abs(I - areaSimp)

PRE = absError*100/I

# calculation of Errors

print("Numerical Value: ", areaSimp)
print("Absolute Error: ", absError)
print("Percentage Relative Error: ", PRE)