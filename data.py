import numpy as np
import math
def angle(x):
    return float(np.radians(x))


wind_theta_dict = {
    "N":0 + 180,
    "NNE": 22.5 + 180,
    "NE":45 + 180,
    "ENE": 67.5 + 180,
    "E":90 + 180,
    "ESE":112.5 + 180,
    "SE":135 + 180,
    "SSE":157.5 + 180,
    "S": 180 + 180,
    "SSW": 202.5 + 180,
    "SW": 225 + 180,
    "WSW": 247.5 + 180,
    "W":270 + 180,
    "NW":315 + 180,
    "NNW": 337.5 + 180
}
def calculate_theta(x,height): # 处理坡度的函数
    return math.atan(height * 0.3048 / (x * 1609.344))

def calculate_theta_w(theta_w,road_theta): # 处理风与道路夹角的函数
    # wind_theta: float, road_theta: list
    for i in range(np.size(road_theta)):
        theta_w[i] = math.radians(float(road_theta[i])) - wind_theta_1 
    
def calculate_x(x2):
    result = []
    for i in range(len(x2)-1):
        result.append(1000*(x2[i+1]-x2[i]))
    return result

def calculate_turn_theta(turn_theta):
    result = []
    for theta in turn_theta: 
        result.append(math.radians(theta))
    return result

def calculate_height(height):
    result = []
    for i in range(len(height)-1):
        result.append(height[i+1]-height[i])
    return result

# men elite UCI
wind_theta_1 = math.radians(wind_theta_dict["NNE"])
road_theta_1 = np.array([
    70,225,180,270,180,150,210,330,
    225,250,220,180,180,225,0,340,60,135,140,230,240,0,230,180
]) # 路面与北方向的夹角
x1 = [0.9,1.8-0.9,3.0-2.0,4.0-2.0,5.0-4.0,6.0-5.0,7.0-6.0,7.4-7.0,8.4-7.4,9.0-8.4,10.0-9.0,11.0-10.0,12.0-11.0,13.8-12.0,15.4-13.8,17.4-15.4,18.1-17.4,19.1-18.1,20-19.1,21.4-20\
    ,22.3-20,24.8-22.3,25.9-24.8,27-25.9]
height_1 = [
    40-33,25-40,6-25,7-6,4-7,4-4,8-4,25-8,21-25,0-21,2-0,10-2,4-10,9-4,18-9,25-18,8-25,7-8,7+3,6+3,4+6,10-4,16-10,31-16
]
theta_w_1 = np.radians(5) * np.ones(24) # 风与路面夹角数据，在下方进行处理


theta_1 = [
    calculate_theta(x1[i],height_1[i]) for i in range(len(x1))
] # 路面坡度数据
turn_index = [0,1,2,3,3,4,7,8,11,12,13,15,16,17,18,19,19] # 拐角对应的片段序号
turn_theta = [angle(120),angle(90),angle(90),angle(60),angle(90),angle(90),angle(80),angle(90),angle(70),angle(90),angle(60),angle(90),angle(60)\
    ,angle(90),angle(90),angle(90) ,angle(90)][::-1]
    # 转弯角度数据
calculate_theta_w(theta_w_1,road_theta_1) # 计算风和路面的夹角

# women elite UCI
Nd_2 = 29 
N_turn_2 = 12
x2 = [0,1.5,2.2,2.6,2.9,4.0,5.0,6.1,6.7,7.3,8.5,9.5,10.4,11.3,13.8,14.9,16.0,17.3,18.5,20,21.55,22.7,23.6,25.0,26.3,27.3,27.9,28.9,30.1,30.4] 
x2 = calculate_x(x2)

wind_theta_2 = math.radians(wind_theta_dict["N"]) # 要改一下，打不开文件了
road_theta_2 = np.array([
    50,225,180,270,180,140,140,130,210,180,200,210,225,330,230,260,220,70,120,150,150,210,210,210,210,270,225,150,180
])
theta_w_2 = np.radians(5) * np.ones(np.size(x2)) # 路、风夹角 
calculate_theta_w(theta_w_2,road_theta_2)

turn_index_2 = [0,1,2,3,5,10,11,14,18,19,22,23] 
turn_theta_2 = [135,90,90,90,45,100,90,110,60,70,90,70]
turn_theta_2 = calculate_turn_theta(turn_theta_2)

height_2 = [8,12,10,9,9,2,2,2,3,2,2,1,1,2,4,0,0,3,3,1,0,5,2,6,4,3,6,8,9]
height_2 = calculate_height(height_2)
theta_2 = [calculate_theta(x2[i],height_2[i]) for i in range(len(x2))] 


x3 = [] 
x4 = []

if __name__ == "__main__":
    print(len(turn_index_2))
    print(len(turn_theta_2))