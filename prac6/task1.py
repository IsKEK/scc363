# Include any required modules

def ComputeMeanVariance(data):
    # TODO
    mean = 0
    variance = 0
    for i in data:
        mean += i
    mean = mean/len(data)
    for i in data:
        variance += (i-mean) ** 2
    variance = variance/len(data)
    return (mean, variance)

if __name__ == "__main__":
    data = range(1,101)
    mean, variance = ComputeMeanVariance(data)
    print(mean)
    print(variance)