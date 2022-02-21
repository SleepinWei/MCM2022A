import numpy as np 
from config import * 
import matplotlib.pyplot as plt 

def angle(x):
    return float(np.radians(x))

from data import x1,turn_index_1,turn_theta_1,theta_1,theta_w_1
from data import x2,turn_index_2,turn_theta_2,theta_2,theta_w_2

x = np.array(x1)
N = np.size(x)  # 赛道分为 N 段
theta = np.array(theta_1)
turn_index = turn_index_1
turn_theta = turn_theta_1
theta_w = theta_w_1
W_s = np.array([12000,11500,12500,11000,11500,12500])
change_ratio = 0.4 # 换人的能量比例

v_w = 6 * np.ones(np.size(x))# 女子风速

def func(W0,W_bal,P,CP,x,theta,v_w,theta_w,k):
    # compute the chagne of W_bal
    if P > CP: 
        W_bal -= (P-CP) * x / v(P,theta,v_w,theta_w,k)
    else:
        W_exp = W0 - W_bal 
        t = float(x) / v(P,theta,v_w,theta_w,k) 
        W_bal = W0 - W_exp * math.pow(math.e,-t/tau(P,CP)) 
    
    return W_bal 

def other_P(P,theta,v_w,theta_w,k):
    # 其他队员的功率
    ratio = 0.4
    return max(v(P,theta,v_w,theta_w,k) * (m * g * math.sin(theta) + mu * m * g - k * ratio * v(P,theta,v_w,theta_w,k) * math.cos(theta_w)),0)
    
def func_W_left(W_team,P,x,theta,v_w,theta_w,mem_no,k):
    return func(float(W_s[mem_no]),float(W_team[mem_no]),P,CP[mem_no],x,theta,v_w,theta_w,k)

def W_change_team(W_team,P,x,theta,v_w,theta_w,mem_no,k):
    for i in range(np.size(W_team)):
        if i == mem_no:
            # 如果是顶风的队员
            W_team[i] = func(float(W_s[i]),float(W_team[i]),P,float(CP[i]),x,theta,v_w,theta_w,k) 
        else:
            P_other = other_P(P,theta,v_w,theta_w,k)

            if P_other > CP[i]: 
                W_team[i] -= (P_other-CP[i]) * x / v(P_other,theta,v_w,theta_w,k)
            else:
                W_exp = W_s[i] - W_team[i] 
                t = float(x) / v(P_other,theta,v_w,theta_w,k) 
                W_team[i] = W_s[i] - W_exp * math.pow(math.e,-t/tau(P_other,CP[mem_no])) 
    # 返回第一个人的剩余能量
                
import turn
def T_total(P,turn_choice):
    # P is a vector 
    result = 0
    global W_s
    W_bal = W_s  # numpy function
    mem_no = 0  # 挡风队员的序号
    for i in range(np.size(P)):
        # W_bal_test = func(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]))
        W_first_test = func_W_left(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),mem_no,k)

        if W_first_test < change_ratio * float(W_s[mem_no]) :
            # 如果能量较小，则换人
            mem_no = (mem_no + 1) % 6
            W_change_team(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),mem_no,k)
        elif func_W_left(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),(mem_no+1)%6,k) < change_ratio * float(W_s[(mem_no+1)%6]): 
            # 如果所有人都能量不足，集体进入休息
            P[i] = 0.99 * CP[mem_no]   
            W_change_team(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),mem_no,k)
        else:
            W_change_team(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),mem_no,k) 
        result += float(x[i])/v(float(P[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),k)

        # 车队转弯的情况
        if i in turn_index : 
            index = turn_index.index(i)
            W_exp = turn.W_exp_turn(float(turn_theta[index]),int(turn_choice[index]))
            t_exp = turn.t_exp_turn(float(turn_theta[index]),int(turn_choice[index])) 
            result += t_exp
            W_bal = W_bal - W_exp   # 整体降低一个能量
            
    return result 

# print(T_total([300,300,300]))

from PSO import PSO 

optimizer = PSO()
optimizer.init(T_total)
optimizer.iter(T_total)
tmin, P ,choice= optimizer.getValue()
optimizer.show()
optimizer.save("./result.txt")

W_bals = [] 
W_bals.append(W_s)
mem_change = []
def cal_W(P):
    W_team = W_s
    mem_no = 0
    mem_change.append(mem_no)
     
    for i in range(np.size(P)): 
        # W_bal = func(W_bal,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),theta_w[i])

        W_first_test = func_W_left(W_team,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),float(theta_w[i]),mem_no,k)
        if W_first_test < change_ratio * W_s[mem_no] :
            mem_no = (mem_no + 1) % 6
        W_change_team(W_team,float(P[i]),float(x[i]),float(theta[i]),float(v_w[i]),(theta_w[i]),mem_no,k)
        W_bals.append(W_team)
        mem_change.append(mem_no)
stage = [i for i in range(N+1)]
cal_W(P)

plt.subplot(2,2,3)
plt.title("W_bal ~ stage ")
plt.plot(stage,W_bals,c="y",label=["mem_" + str(i) for i in range(6)])
plt.legend()

plt.savefig("./team.jpg")

plt.figure(2)
plt.title("mem_change ~ stage")
plt.plot(stage,mem_change,label="mem_change")
plt.legend()

plt.show()