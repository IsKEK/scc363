# from dhCheck_Task1 import dhCheckCorrectness
def Task1(a, b, c, AV, point1, point2, data):
    # part 1
    # find cdf at point 1 (prob that it's less than point 1)
    prob1 = (point1-a)**2/((b-a)*(c-a))
    # find prob that it's more than point 2 (1 - cdf at point 2)
    prob2LessThan = 1-(b-point2)**2/((b-a)*(b-c))
    prob2 = 1 - prob2LessThan
    SLE = (a+b+c)/3
    EF = SLE/AV

    # part 2
    # calculate mean and variance 
    mean = sum(data)/len(data)
    v_data = [(x-mean)**2 for x in data]
    variance = sum(v_data)/len(data)
    ARO = mean 
    ALE = ARO*SLE
    return (prob1, prob2, EF, mean, variance, ALE)

a = 1000
b = 10000
c = 4000
point1 = 2000
point2 = 8000
AV = 10000
data = [5, 7, 3, 9, 7, 4, 5, 6, 8, 2]
result = Task1(a, b, c, AV, point1, point2, data)
print(result)