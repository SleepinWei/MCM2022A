import numpy as np 
import random

class PSO():
    Xmin = 10 
    Xmax = 1000 
    Vmax = 10
    Vmin = -10
    Nd = 24# dimension  
    N_turn = 17 # the number of turns 
    Np = 500 # 粒子个数
    Nm = 300 # 迭代次数
    C1 = 0

    w = 0.8 # 惯性系数
    c1 = 0.5 # 个体最优系数
    c2 = 0.5 # 全局最优系数

    p = np.zeros((Np,Nd)) # 粒子的位置
    p_mode = np.zeros((Np,N_turn)) #  表示弯角的数量
    v = np.zeros((Np,Nd)) # Np个粒子的速度

    C_best_p = 1e20 * np.ones((Np,1)) # Np 个粒子在 N,m 次迭代中的最优值
    x_best_p = 1e2 * np.ones((Np,Nd)) # Np 个粒子在Nm次迭代中的最优解
    mode_best_p = 1 * np.ones((Np,N_turn))

    C_best_g = 1e20 # 全局最优
    x_best_g = Xmax * 10 # 全局最优解
    mode_best_g = 1 * np.ones(N_turn) 

    iters = [] 
    x_best_s = [] 
    C_best_s = [] 
    turn_choice_s = []

    def init(self,func):
        # initialize the position of points 
        for i in range(self.Np):
            self.p[i,:] = self.Xmin + np.random.rand(1,self.Nd) \
                * (self.Xmax-self.Xmin) 
            self.v[i,:] = self.Vmin + np.random.rand(1,self.Nd)* (self.Vmax-self.Vmin) 
            self.p_mode[i,:] = 0 + np.random.randint(0,3,(1,self.N_turn))
        
            self.C1 = func(self.p[i,:],self.p_mode[i,:]) 
        
        # 更新个体最优
            if self.C_best_p[i] > self.C1: 
                self.C_best_p[i] = self.C1
                self.x_best_p[i,:] = self.p[i,:]
                self.mode_best_p[i,:] = self.p_mode[i,:]

        # 更新全局最优
            if self.C_best_g > self.C1:
                self.C_best_g = self.C1
                self.x_best_g = self.p[i,:]
                self.mode_best_g = self.p_mode[i,:]
    
    def iter(self,func): 
        for k in range(self.Nm): 
            for i in range(self.Np):

                self.v[i,:] = self.w * self.v[i,:] + random.random()*self.c1 * (self.x_best_p[i] - self.p[i,:]) + \
                    random.random() * self.c2 *  (self.x_best_g - self.p[i,:])
                
                for j in range(self.Nd):
                    if self.v[i,j] > self.Vmax :
                        self.v[i,j] = self.Vmax
                    
                    if self.v[i,j] < self.Vmin:
                        self.v[i,j] = self.Vmin 
                    
                self.p[i,:] = self.p[i,:] + self.v[i,:]
                # 使用随机数的方式决定是否更新
                self.p_mode[i,:] = np.random.randint(0,3,(1,self.N_turn)) if random.random() > 0.8 else self.p_mode[i,:]

                for j in range(self.Nd):
                    if self.p[i,j] > self.Xmax:
                        self.p[i,j] = self.Xmax
                        
                    if self.p[i,j] < self.Xmin:
                        self.p[i,j] = self.Xmin
                        
                self.C1 = func(self.p[i,:],self.p_mode[i,:])

                if self.C_best_g > self.C1:
                    self.C_best_g = self.C1
                    self.x_best_g = self.p[i,:]
                    self.mode_best_g = self.p_mode[i,:]

            # print("iter: "+str(k)+" C_best : " + str(self.C_best_g) + " x_best : " + str(self.x_best_g))
            self.iters.append(k)
            self.x_best_s.append(self.x_best_g)
            self.C_best_s.append(self.C_best_g)
            self.turn_choice_s.append(self.mode_best_g)

    def show(self): 
        print("C_best_g : " + str(self.C_best_g))        
        print("x_best_g : " + str(self.x_best_g))
        print("mode_best_g : ",end="")
        for el in self.mode_best_g:
            print(str(el) + " ",end="")
        print("")
        import matplotlib.pyplot as plt 

        plt.subplot(2,2,1)
        plt.title("x ~ iteration")
        plt.plot(self.iters,self.x_best_s,label=["x"+str(i) for i in range(self.Nd)])
        plt.legend()

        plt.subplot(2,2,2)
        plt.title("Value ~ iterations")
        plt.plot(self.iters,self.C_best_s,label="value")
        plt.legend()

        plt.subplot(2,2,4)
        plt.title("turn choice ~ iterations")
        plt.plot(self.iters,self.turn_choice_s,label=["turn_"+ str(i) for i in range(self.N_turn)])
        plt.legend()
        # plt.show()

    def getValue(self):
        return self.C_best_g,self.x_best_g,self.mode_best_g

