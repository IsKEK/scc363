## Arithmetic mean and population variance
def ComputeMeanVariance(data):
    # TODO
    mean = sum(data)/len(data)
    v_data = [(x-mean)**2 for x in data]
    variance = sum(v_data)/len(data)
    return (mean, variance)

data = range(1, 101)
result = ComputeMeanVariance(data)
print(result)

## Geometric distribution
def GeometricDistribution(p, k):
    # TODO
    mean = 1/p
    variance = (1-p)/p**2
    prob = 1-(1-p)**k
    return (mean, variance, prob)

q = 0.98
p = 1-q
k = 50
result = GeometricDistribution(p, k)
print(result)

## Pareto distribution
def ParetoDistribution(alpha, xm, x):
    # TODO
    if alpha > 1:
        mean = alpha*xm/(alpha-1)
    else:
        mean = 'inf'
    if alpha > 2:
        variance = xm**2*alpha/((alpha-1)**2*(alpha-2))
    elif alpha > 1:
        variance = 'inf'
    else:
        variance = 'nan'
    if x >= xm:
        prob = (xm/x)**alpha
    else:
        prob = 1
    return (mean, variance, prob)

alpha = 2.5
xm = 1
x = 5
result = ParetoDistribution(alpha, xm, x)
print(result)

## Triangular distribution
import matplotlib.pyplot as plt
def TriangularDistribution(a, b, c, data):
    # TODO
    pdf = [0]*len(data)
    for i in range(len(data)):
        if data[i] < a:
            pdf[i] = 0
        elif data[i] < c:
            pdf[i] = 2*(data[i]-a)/((b-a)*(c-a))
        elif data[i] == c:
            pdf[i] = 2/(b-a)
        elif data[i] <= b:
            pdf[i] = 2*(b-data[i])/((b-a)*(b-c))
        else:
            pdf[i] = 0
    cdf = [0]*len(data)
    for i in range(len(data)):
        if data[i] <= a:
            cdf[i] = 0
        elif data[i] <= c:
            cdf[i] = (data[i]-a)**2/((b-a)*(c-a))
        elif data[i] < b:
            cdf[i] = 1-(b-data[i])**2/((b-a)*(b-c))
        else:
            cdf[i] = 1
    mean = (a+b+c)/3
    variance = (a**2+b**2+c**2-a*b-a*c-b*c)/18
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Triangular Distribution')
    axs[0].plot(data, pdf, marker='o')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Probability')
    axs[1].plot(data, cdf, marker='*')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('Cumulative Probability')
    plt.show()
    plt.savefig('triangular_distribution.svg', format='svg')
    return (mean, variance)
a = 100
b = 50000
c = 20000
data = range(1, 60001)
result = TriangularDistribution(a, b, c, data)
print(result)
