from tokenize import Double
import numpy as np 
from config import * 
import matplotlib.pyplot as plt 

def angle(x):
    return float(np.radians(x))
N = 24  # 赛道分为 N 段
# W_bal = W0 # initialize W_bal 
# x1 = [0.9,1.8-0.9,3.0-2.0,4.0-2.0,5.0-4.0,6.0-5.0,7.0-6.0,7.4-7.0,8.4-7.4,9.0-8.4,10.0-9.0,11.0-10.0,12.0-11.0,13.8-12.0,15.4-13.8,17.4-15.4,18.1-17.4,19.1-18.1,20-19.1,21.4-20\
#     ,22.3-20,24.8-22.3,25.9-24.8,27-25.9]
# height = [

# ]
# theta_1 = [

# ]
# turn_index = [0,1,2,3,3,4,7,8,11,12,13,15,16,17,18,19,19]
# turn_theta = [angle(120),angle(90),angle(90),angle(60),angle(90),angle(90),angle(80),angle(90),angle(70),angle(90),angle(60),angle(90),angle(60)\
#     ,angle(90),angle(90),angle(90) ,angle(90)][::-1]
# x2 = [] 
# x3 = [] 
# x4 = []
from data import x1,turn_index_1,turn_theta_1,theta_1,theta_w_1
from data import x2,turn_index_2,turn_theta_2,theta_2,theta_w_2

# x = np.array(x1) 
# theta = np.array(theta_1)
x = np.array(x2)
theta = np.array(theta_2)
turn_index = turn_index_2
turn_theta = turn_theta_2
theta_w = theta_w_2

v_w = 11.3 * np.ones(np.size(x))# 女子风速

def func(W_bal,P,x,theta,v_w,theta_w):
    # compute the chagne of W_bal
    if P > CP: 
        W_bal -= (P-CP) * x / v(P,theta,v_w,theta_w)
    else:
        W_exp = W0 - W_bal 
        t = float(x) / v(P,theta,v_w,theta_w) 
        W_bal = W0 - W_exp * math.pow(math.e,-t/tau(P)) 
    
    return W_bal 

import turn
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

# print(T_total([300,300,300]))

from PSO import PSO 

optimizer = PSO()
optimizer.init(T_total)
optimizer.iter(T_total)
tmin, P ,choice= optimizer.getValue()
optimizer.show()

W_bals = [] 
W_bals.append(W0)
def cal_W(P):
    W_bal = W0
    for i in range(np.size(P)): 
        W_bal = func(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),theta_w[i])
        W_bals.append(W_bal)
stage = [i for i in range(N+1)]
cal_W(P)

plt.subplot(2,2,3)
plt.title("W_bal ~ stage ")
plt.plot(stage,W_bals,c="y",label="W_bal")
plt.legend()

plt.show()

