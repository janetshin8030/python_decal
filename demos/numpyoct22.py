import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(0,2*np.pi, 100)
y= np.sin(x)
plt.figure()
plt.plot(x,y)
plt.show()
arr1= np.array([1,2,3])
arr2= np.array([4,5,6])
arr3= arr1+arr2
print(arr3)
print(f'adding two lists: {arr1 +arr2} ')

def loopSum():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)
    return sum
loopSum()

print(np.sum(np.arange(101)))

