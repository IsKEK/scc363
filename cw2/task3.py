from scipy.optimize import curve_fit
import numpy as np
# from dhCheck_Task3 import dhCheckCorrectness
def Task3(x, y, num1, num2, num3, num4, bound_y):
    def fn(xdata, a, b0, b1, b2, b3, b4):
        return a+b0*xdata[0]+b1*xdata[1]+b2*xdata[2]+b3*xdata[3]+b4*xdata[4]
    weights, pcov = curve_fit(fn, x, y)
    num5 = 0
    return (weights, num5)

x = np.array([[5,4,8,8,2,5,5,7,8,8], [3,7,7,2,2,5,10,4,6,3],[8,3,6,7,9,10,6,2,2,3],[8,3,6,7,9,10,6,2,2,3],[9,3,9,3,10,4,2,3,7,5],[4,9,6,6,10,3,8,8,4,6]])
y = np.array([176,170,215,146,228,145,183,151,160,151])
num1 = 5
num2 = 6
num3 = 8
num4 = 4
bound_y = 160
result = Task3(x, y, num1, num2, num3, num4, bound_y)
print(result[0])