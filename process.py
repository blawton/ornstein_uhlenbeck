"""
Numerically approximating the solution to the Ornstein-Uhlenbeck Process with the Euler-Maruyama method
For simplicity, program assumes domain of 0 to 1 and other parameters should be scaled accordingly

Author: Ben Lawton
"""

import numpy as np
import matplotlib.pyplot as plt

N=400
gamma = 2
y0 = 2
mu=1
sigma = 5

step= 1/N

#Functions Used
def generate(step):
    return(np.random.normal(0, sigma*step))

def dy(sigma, theta, y, step):
    return(theta*(mu-y)*step + generate(step))

#Recursively generating samples

array=np.zeros(N)
array[0]=y0

for i in range(1, N):
    array[i]=array[i-1]+dy(sigma, gamma, array[i-1], step)
    
#Plotting results
plt.plot(np.array(range(len(array)))/N, array, label="process")
plt.xlabel("t (time)")
plt.ylabel("Y_t")
plt.hlines(mu, color="black", xmin=plt.gca().get_xlim()[0], xmax=plt.gca().get_xlim()[1], linestyle="dashed", label=u"\u03bc")
plt.legend()
plt.tight_layout()

params = [gamma, y0, mu, sigma, N]
plt.savefig("graphs/Process_" + "_".join([str(param) for param in params])+ "_steps.png")
plt.show()
    
    
