from scipy.optimize import linprog
# from dhCheck_Task4 import dhCheckCorrectness
def Task4(c, safeguard_effect, maintenance_load, se_bound, ml_bound, x_bound, x_initial):
    # TODO
    # A1 = [-abs(safeguard_effect[0])]
    A1 = []
    for i in range(5):
        # A1.append(-abs(safeguard_effect[i+1]*x_initial[i]))
        A1.append(-abs(safeguard_effect[i+1]))
    Aie = [A1, maintenance_load]
    # print(Aie)
    se_initial = safeguard_effect[0]
    for i in range(5):
        se_initial += safeguard_effect[i+1]*x_initial[i]
    se_bound = se_bound - se_initial
    ml_initial = 0
    for i in range(5):
        ml_initial += maintenance_load[i]*x_initial[i]
    ml_bound = ml_bound - ml_initial
    bie = [-se_bound, ml_bound]
    # print(bie)
    total = linprog(c, A_ub=Aie, b_ub=bie, bounds=x_bound)
    x = total.x
    for i in range(5):
        print(x[i])
        print(x_initial[i])
        x[i] = x[i] - x_initial[i]
    return(x)

x_initial = [3, 5, 4, 2, 1]
safeguard_effect = [6, 3, 5, 4, 8, 9]
maintenance_load = [1, 2, 5, 3, 3]
se_bound = 1000
ml_bound = 800
c = [11, 6, 8, 10, 9]
bound1 = (3, 30)
bound2 = (5, 50)
bound3 = (4, 20)
bound4 = (2, 45)
bound5 = (1, 50)
x_bound = [bound1, bound2, bound3, bound4, bound5]
result = Task4(c, safeguard_effect, maintenance_load, se_bound, ml_bound, x_bound, x_initial)
print(result)