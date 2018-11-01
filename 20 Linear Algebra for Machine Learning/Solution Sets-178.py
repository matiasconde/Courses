## 2. Inconsistent Systems ##

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,1000)

y1 = 5/4-2*x
y2 = 5/2-2*x

plt.plot(x,y1,color="blue")
plt.plot(x,y2,color="blue")
plt.show()

## 3. Singular Matrix ##

a = np.asarray([[8,4],[4,2]],dtype=np.float32)
print(np.linalg.det(a))

## 5. Homogenous Systems ##

def test_homog(x3):
    x1 = 4/3*x3
    x2=0
    
    result1 = 6*x1+10*x2-8*x3==0
    result2 = -6*x1-4*x2+8*x3==0
    result3 = 3*x1+0.5*x2-4*x3==0
    
    return result1 and result2 and result3
        
b_one = test_homog(1)
b_two = test_homog(-10)
    