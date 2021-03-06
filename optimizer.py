import numpy as np 
from config import * 
import matplotlib.pyplot as plt 

def angle(x):
    return float(np.radians(x))

from data import x1,turn_index_1,turn_theta_1,theta_1,theta_w_1
from data import x2,turn_index_2,turn_theta_2,theta_2,theta_w_2
from data import x3,turn_index_3,turn_theta_3,theta_3,theta_w_3
from data import x4,turn_index_4,turn_theta_4,theta_4,theta_w_4

x = np.array(x1)
N = np.size(x)  # 赛道分为 N 段
theta = np.array(theta_1)
turn_index = turn_index_1
turn_theta = turn_theta_1
theta_w = theta_w_1

v_w = 6 * np.ones(np.size(x))# 女子风速

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
optimizer.save("result.txt")
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

distance = []
distance.append(0)
dist = 0
for i in range(len(stage)-1):
    dist += float(x[i])  
    distance.append(dist/1000)
with open("W'.txt","w") as file:
    file.write(str(W_bals))
    file.write("\n")
    file.write(str(distance))
plt.figure(2)
plt.style.use("bmh")
plt.title("W' ~ distance")
plt.xlabel("distance/km")
plt.ylabel("W'/J")
plt.plot(distance,W_bals,label="W'")
plt.legend()

plt.figure(3)
plt.style.use("bmh")
plt.title("T ~ iterations")
plt.xlabel("iterations")
plt.ylabel("T")
plt.plot(optimizer.iters,optimizer.C_best_s,label="T")
plt.legend()


plt.savefig("./individual.jpg")

plt.show()

