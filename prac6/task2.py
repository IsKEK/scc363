# Include any required modules
def GeometricDistribution(p, k):
    mean = 1/p
    variance = (1-p)/p**2
    prob = 1 - (1-p)**k
    return (mean, variance, prob)

if __name__ == "__main__":
    # p = 0.98 OWIBKA
    q = 0.98
    p = 1-q
    k = 50
    mean, variance, prob = GeometricDistribution(p, k)
    print(mean)
    print(variance)
    print(prob)