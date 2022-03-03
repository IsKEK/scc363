# Include any required modules
from scipy.optimize import linprog #needed for linear program
def LinearProgram(c, Aie, bie, Aeq, beq, bound):
    # for i in range(5):
    #     A 
    newAie = [-x for x in Aie]
    A1 = []
    A2 = []
    b = [-bie, beq]
    for i in range(5):
        A1.append(newAie[i])
        A2.append(Aeq[i])
    A = [A1, A2]
    x0_b = x1_b = x2_b = (0, 10)
    x3_b = x4_b = (0, 12)
    bounds=[x0_b, x1_b, x2_b, x3_b, x4_b]
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
    x = res['x']
    return (x)

c = [8, 8, 15, 8, 12]
bie = 100
beq = 150
Aie = [4, 4.6, 7.2, 4, 5.5] 
Aeq = [4, 4.3, 4, 5, 6]
bound = [10, 10, 10, 12, 12]
result = LinearProgram(c, Aie, bie, Aeq, beq, bound)
print(result)