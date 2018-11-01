## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np
import sympy

h,x,y = sympy.symbols('h x y')

y = -2*x-h+3

limit = sympy.limit(y,h,0)

print(type(limit))

x = np.linspace(-5,6,110)
z = 2*x+3 

plt.plot(x,z)
plt.show()


## 6. Power Rule ##

slope_one = 5*(2**4)
slope_two = 9*(0**8)

## 7. Linearity Of Differentiation ##

slope_three = 5*(1**4)-1
slope_four = 3*(2**2)-2*2

## 8. Practicing Finding Extreme Values ##

rel_max = []
rel_min = []

critical_points = [0,2/3]

for point in critical_points:
    if (3*((point-0.1)**2)-2*(point-0.1))<0 and (3*((point+0.1)**2)-2*(point+0.1))>0: rel_min.append(point)
    elif (3*((point-0.1)**2)-2*(point-0.1))>0 and (3*((point+0.1)**2)-2*(point+0.1))<0: rel_max.append(point)
        
        