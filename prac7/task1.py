# Include any required modules
from scipy.stats import norm #needed for random sampling
import matplotlib.pyplot as plt #needed for plotting histogram

def SampleNormal(mu, sigma, num, l, u):
    failures = 0
    randomNumbers = norm.rvs(loc=mu, scale=sigma, size=num)
    for n in randomNumbers:
        if n>u or n<l:
            failures += 1
    # fig, ax = plt.subplots(1, 1)
    # plt.hist(randomNumbers)
    # ax.legend(loc='best', frameon=False)
    # plt.show()
    failure_prob = failures/len(randomNumbers)
    cdf = norm.cdf(randomNumbers, loc=mu, scale=sigma)
    thrFails = 0
    for i in cdf:
        if i>u or i<l:
            thrFails += 1
    theoretic_failure_prob = norm.cdf(l, mu, sigma)+1-norm.cdf(u, mu, sigma)
    plt.hist(randomNumbers)
    plt.show()
    return (failure_prob, theoretic_failure_prob)

# def SampleNormal(mu, sigma, num, l, u):
#     # TODO
#     s = norm.rvs(mu, sigma, num)
#     failure_count = 0
#     for i in range(len(s)):
#         if s[i] > u or s[i] < l:
#             failure_count = failure_count+1
#     failure_prob = failure_count/len(s)
#     theoretic_failure_prob = norm.cdf(l, mu, sigma)+1-norm.cdf(u, mu, sigma)
#     plt.hist(s)
#     plt.show()
#     plt.savefig('samplenormal', format='svg')
#     return(failure_prob, theoretic_failure_prob)

u = 3
l = -3
mu = 0.5
sigma = 1.5
num = 10000
result = SampleNormal(mu, sigma, num, l, u)
print(result)