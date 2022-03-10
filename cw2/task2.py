from scipy.stats import lognorm
from scipy.stats import pareto
# from dhCheck_Task2 import dhCheckCorrectness
def Task2(mu, sigma, xm, alpha, num, point1, point2, point3):
    rpPareto = pareto.rvs(alpha, size=num)
    rpLogNorm = lognorm.rvs(sigma, size=num)
    rpTotal = [0]*num
    for i in range(num):
        rpTotal[i] = rpLogNorm[i] + rpPareto[i]
    prob1 = 0
    prob2 = 0
    for i in range(num):
        if rpTotal[i] > point1:
            prob1 += 1
            if rpTotal[i] > point2 and rpTotal[i] < point3:
                prob2 += 1
    prob1 = prob1/num
    prob2 = prob2/num
    return (prob1, prob2)

mu = 0
sigma = 5
xm = 1
alpha = 3
num = 50000
point1 = 30
point2 = 50
point3 = 100
result = Task2(mu, sigma, xm, alpha, num, point1, point2, point3)
print(result)