import math 
mu = 0.001 
m = 70 
g = 9.8 
k = 3 
CP = 354.12
W0 = 11429.3 
# CP = 344.05
# W0 = 14055.71
# CP = 326.61
# W0 = 7946.05
# CP = 326.31
# W0 = 7466.11

def v(P,theta,v_w,theta_w):
    b = mu * m * g - k * v_w * math.cos(theta_w) + m * g * math.sin(math.radians(theta)) 
    a = k 
    c = -P 
    return (-b + math.sqrt(b**2 - 4 * a *c )) / (2 * a )
    
# 在什么 P 下休息最佳

def DCP(P):
    return CP - P 

def tau(P):
    # P stands for power at rest 
    return 546 * math.pow(math.e,-0.01*DCP(P)) + 316 

if __name__ == "__main__":
    import matplotlib.pyplot as plt 
    import numpy as np
    theta = 0
    k = np.arange(0,10,0.1)
    P = 500 
    v_w = 1
    v_s = [v(P,theta,v_w,180,K) for K in k]
    plt.plot(k,v_s)
    plt.show()