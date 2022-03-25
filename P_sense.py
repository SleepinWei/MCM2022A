CP = 354.12
W0 = 11429.3
import numpy as np
import math
from config import * 
from data import x1,turn_index_1,theta_w_1,turn_theta_1,road_theta_1,theta_1
import turn

x = x1
turn_index = turn_index_1
theta_w = theta_w_1
turn_theta = turn_theta_1
theta = theta_1
road_theta = road_theta_1
v_w = 6 * np.ones(24) 
turn_choice = [1.0,1.0,0.0,1.0,2.0,0.0,1.0,2.0,2.0,1.0,1.0,1.0,0.0,2.0,2.0,2.0,0.0]
def func(W_bal,P,x,theta,v_w,theta_w):
    # compute the chagne of W_bal
    if P > CP: 
        W_bal -= (P-CP) * x / v(P,theta,v_w,theta_w)
    else:
        W_exp = W0 - W_bal 
        t = float(x) / v(P,theta,v_w,theta_w) 
        W_bal = W0 - W_exp * math.pow(math.e,-t/tau(P)) 
    
    return W_bal
def T_total(P,turn_choice):
    # P is a vector 
    result = 0
    W_bal = W0 
    for i in range(np.size(P)):
        W_bal_test = func(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]))

        if W_bal_test < 0: 
            # result += k* W_bal**2
            P[i] = CP * 0.99
            W_bal = func(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]))
        else:
            W_bal = W_bal_test
        result += float(x[i])/v(float(P[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]))

        if i in turn_index : 
            index = turn_index.index(i)
            W_exp = turn.W_exp_turn(turn_theta[index],int(turn_choice[index]))
            t_exp = turn.t_exp_turn(turn_theta[index],int(turn_choice[index])) 
            result += t_exp
            W_bal -= W_exp 
            
    return result 
P = [267.9259770645792 , 350.5787999999834 , 350.57882728764173 , 350.5787999999455 , 350.578799977726 , 350.5788000000449 , 350.57880979761626 , 350.57888071049695 , 362.37678927057374 , 350.57880003423116 , 350.57879999990195 , 350.5788001369567 , 350.57880000004644 , 297.25238672970625 , 350.5788001013305 , 350.578799889576 , 350.57879999999534 , 307.688779554404 , 350.5788000001243 , 350.5787999999762 , 350.57879999993094 , 350.5788000000631 , 350.5788000000815 , 162.72863509825515]
with open("P_sense.txt","w") as file:
    for i in range(len(P)): 
        p1 = P[:i] + [P[i] * 1.05] + P[i+1:]
        
        t1 = T_total(p1,turn_choice)
        p2 = P[:i] +[ P[i] * 0.95 ]+ P[i+1:]
        t2 = T_total(p2,turn_choice)

        file.write(str(t1)+"\n")
        file.write(str(t2)+"\n")
        file.write(str((t2-t1)/t1/0.1)+"\n")

    
        
     