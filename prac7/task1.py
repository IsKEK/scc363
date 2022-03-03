# Include any required modules
from scipy.stats import norm #needed for random sampling
import matplotlib.pyplot as plt #needed for plotting histogram

def SampleNormal(mu, sigma, num, l, u):
    failures = 0
    randomNumbers = norm.rvs(loc=mu, scale=sigma, size=num)
    for n in randomNumbers:
        print(n)
        if n>u or n<l:
            failures += 1
    fig, ax = plt.subplots(1, 1)
    ax.hist(randomNumbers, density=True, histtype='stepfilled', alpha=0.2)
    # ax.legend(loc='best', frameon=False)
    plt.show()
    failure_prob = failures/len(randomNumbers)
    cdf = norm.cdf(randomNumbers, loc=mu, scale=sigma)
    thrFails = 0
    for i in cdf:
        if i>u or i<l:
            thrFails += 1
    theoretic_failure_prob = thrFails/len(cdf)
    return (failure_prob, theoretic_failure_prob)

u = 3
l = -3
mu = 0.5
sigma = 1.5
num = 10000
result = SampleNormal(mu, sigma, num, l, u)
print(result)