import math 
mu = 0.001 
m = 70 
g = 9.8 
k = 5 
# P0 = 500 
# v_w = 5
CP = 300
# theta = 5 
W0 = 20000

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
    pass