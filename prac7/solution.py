## Task 1: Random sampling
from scipy.stats import norm
import matplotlib.pyplot as plt
def SampleNormal(mu, sigma, num, l, u):
    # TODO
    s = norm.rvs(mu, sigma, num)
    failure_count = 0
    for i in range(len(s)):
        if s[i] > u or s[i] < l:
            failure_count = failure_count+1
    failure_prob = failure_count/len(s)
    theoretic_failure_prob = norm.cdf(l, mu, sigma)+1-norm.cdf(u, mu, sigma)
    plt.hist(s)
    plt.show()
    plt.savefig('samplenormal', format='svg')
    return(failure_prob, theoretic_failure_prob)

mu, sigma, num, l, u = 0.5, 1.5, 10000, -3, 3
result = SampleNormal(mu, sigma, num, l, u)
print(result)

## Task 2: Linear programming
from scipy.optimize import linprog
def LinearProgram(c, Aie, bie, Aeq, beq, bound):
    # TODO
    x = linprog(c, Aie, bie, Aeq, beq, bound)
    return(x)

bound1 = (0, 10)
bound2 = (0, 10)
bound3 = (0, 10)
bound4 = (0, 12)
bound5 = (0, 12)
bound = [bound1, bound2, bound3, bound4, bound5]
Aie =[[-4, -4.6, -7.2, -4, -5.5], [4, 4.3, 4, 5, 6]]
bie = [-100, 150]
c = [8, 8, 15, 8, 12]
Aeq = None
beq = None
result = LinearProgram(c, Aie, bie, Aeq, beq, bound)
print(result)

## Task 3: Linear regression
from scipy.optimize import curve_fit
import numpy as np
def LinearRegression(x, y):
    # TODO
    def fn(xdata, a, b0, b1, b2, b3):
        return a+b0*xdata[0]+b1*xdata[1]+b2*xdata[2]+b3*xdata[3]
    weights, pcov = curve_fit(fn, x, y)
    return (weights)

x = np.array([[8,3,6,7,9,10,6,2,2,3],[9,3,9,3,10,4,2,3,7,5],[4,9,6,6,10,3,8,8,4,6],[1,1,6,8,10,2,6,5,1,4]])
y = np.array([600.8377,371.3878,680.2967,592.7107,962.5547,532.6802,528.3036,406.0273,354.8229,433.6177])
result = LinearRegression(x, y)
print(result)
