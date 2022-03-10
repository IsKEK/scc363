# Include any required modules
from tkinter.tix import MAX


def ParetoDistribution(alpha, xm, x):
    if alpha > 1:
        mean = (alpha*xm)/(alpha-1)
    else:
        mean = MAX
    if alpha > 2:
        # variance = (xm**2/(alpha-1)**2)*(alpha/alpha-2) 
        variance = xm**2*alpha/((alpha-1)**2*(alpha-2))
    elif alpha in range(1, 2):
        variance = MAX
    else:
        variance = None
    if x >= xm:
        probLessThan = 1 - (xm/x)**alpha
        prob = 1 - probLessThan
        # prob = prob * 100
    else:
        prob = 1
    return (mean, variance, prob)

if __name__ == "__main__":
    alpha = 2.5
    xm = 1
    x = 5
    mean, variance, prob = ParetoDistribution(alpha, xm, x)
    print(mean)
    print(variance)
    print(prob)