import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calc_pi(iterations):
    x = np.random.uniform(-1,1,iterations)
    y = np.random.uniform(-1,1,iterations)
    z = ((x**2 + y**2)**5 < 1)
    return sum(z)/iterations*4


# Create a generator to iterate over multiples of 10
def mult10(start=1,end=10000):
    start = 1
    while start <= end:
        yield start
        start *= 10


# Simulate pi for multiples of 10 until you get to num
def sim_pi(num):
    l = []
    for i in mult10(end=num):
        l.append([i,calc_pi(i)])
    return pd.DataFrame(l, columns=['Iterations','Estimated Pi'])


np.random.seed(3) #lucky number 3
df = sim_pi(100000)
print(df)

df.plot(x='Iterations', y='Estimated Pi', logx=True)
plt.xlabel('Iterations (Log scale)')
plt.title('Estimating pi')
plt.axhline(y=np.pi, color='r', label='Actual Pi',alpha=.5)
plt.legend()
plt.savefig('graphs/estimating_pi.png')
plt.show()
