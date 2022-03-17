from scipy.optimize import linprog
# from dhCheck_Task4 import dhCheckCorrectness
def Task4(c, safeguard_effect, maintenance_load, se_bound, ml_bound, x_bound, x_initial):
    # TODO
    # A1 = [-abs(safeguard_effect[0])]
    A1 = []
    for i in range(5):
        A1.append(-abs(safeguard_effect[i+1]*x_initial[i]))
    Aie = [A1, maintenance_load]
    bie = [-se_bound, ml_bound]
    x = linprog(c, A_ub=Aie, b_ub=bie, bounds=x_bound)
    return(x)

x_initial = [3, 5, 4, 2, 1]
safeguard_effect = [6, 3, 5, 4, 8, 9]
maintenance_load = [1, 2, 5, 3, 3]
se_bound = 1000
ml_bound = 800
c = [11, 6, 8, 10, 9]
bound1 = (0, 30)
bound2 = (0, 50)
bound3 = (0, 20)
bound4 = (0, 45)
bound5 = (0, 50)
x_bound = [bound1, bound2, bound3, bound4, bound5]
result = Task4(c, safeguard_effect, maintenance_load, se_bound, ml_bound, x_bound, x_initial)
print(result)

# ASK ABOUT SAFEGUARD EFFECT!!!