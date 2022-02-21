import numpy as np 
from config import * 

W_turn = [200,300,400] 
t_turn = [10,8,6]
kw_turn = [0.15,0.14,0.12] 
kt_turn = [0.1,0.09,0.08]

def W_exp_turn(theta, mode):
    return W_turn[mode] * math.pow(math.e,kw_turn[mode]*theta)

def t_exp_turn(theta,mode):
    return t_turn[mode] * math.pow(math.e,kt_turn[mode] * theta)

if __name__ == "__main__":
    thetas = np.arange(0,math.pi,0.01)
    Ws_1 = [W_exp_turn(theta,0) for theta in thetas]
    Ws_2 = [W_exp_turn(theta,1) for theta in thetas]
    Ws_3 = [W_exp_turn(theta,2) for theta in thetas]

    ts_1 = [t_exp_turn(theta,0) for theta in thetas]
    ts_2 = [t_exp_turn(theta,1) for theta in thetas]
    ts_3 = [t_exp_turn(theta,2) for theta in thetas]


    import matplotlib.pyplot as plt 
    plt.subplot(1,2,1)
    plt.plot(thetas,Ws_1,label="1")
    plt.plot(thetas,Ws_2,label="2")
    plt.plot(thetas,Ws_3,label="3")
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(thetas,ts_1,label="1")
    plt.plot(thetas,ts_2,label="2")
    plt.plot(thetas,ts_3,label="3")
    plt.legend()

    plt.show()

