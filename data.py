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
# wind_theta_1 = math.radians(wind_theta_dict["NE"])
wind_theta_1 = math.radians(45 + 180)
road_theta_1 = np.array([
    70,225,180,270,180,150,210,330,
    225,250,220,180,180,225,0,340,60,135,140,230,240,0,230,180
]) # 路面与北方向的夹角
x1 = [0.9,1.8-0.9,3.0-2.0,4.0-3.0,5.0-4.0,6.0-5.0,7.0-6.0,7.4-7.0,8.4-7.4,10.0-8.4,11.0-10.0,12.0-11.0,13.8-12.0,15.4-13.8,17.4-15.4,18.1-17.4,19.1-18.1,20-19.1,21.4-20\
    ,22.3-20,24.8-22.3,25.9-24.8,26.5-25.9,27-26.5]
x1 = [x * 1609 for x in x1]
height_1 = [
    40-33,25-40,6-25,7-6,4-7,4-4,8-4,25-8,21-25,0-21,2-0,10-2,4-10,9-4,18-9,25-18,8-25,7-8,7+3,6+3,4+6,10-4,16-10,31-16
]
theta_w_1 = np.radians(5) * np.ones(len(x1)) # 风与路面夹角数据，在下方进行处理


theta_1 = [
    calculate_theta(x1[i],height_1[i]) for i in range(len(x1))
] # 路面坡度数据
turn_index_1 = [0,1,2,3,3,4,7,8,11,12,13,15,16,17,18,19,19] # 拐角对应的片段序号
turn_theta_1 = [angle(120),angle(90),angle(90),angle(60),angle(90),angle(90),angle(80),angle(90),angle(70),angle(90),angle(60),angle(90),angle(60)\
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

height_2 = [8,12,10,9,9,2,2,2,3,2,2,1,1,2,4,0,0,3,3,1,0,5,3,2,6,4,3,6,8,9]
height_2 = calculate_height(height_2)
theta_2 = [calculate_theta(x2[i],height_2[i]) for i in range(len(x2))] 

Nd_3 = 27 
N_turn_3 = 26 
x3 = [0,0.6,1.1,1.3,1.5,1.7,2.5,3.1,3.6,6,6.5,7.3,8,8.2,9.2,9.7,9.9,10.4,10.5,10.9,11.3,11.5,11.7,11.8,12.1,12.7,12.8,13.7] 
x3 = calculate_x(x3)
x3 = [x * 1.609 for x in x3]

wind_theta_3 = math.radians(wind_theta_dict["NE"]) # 要改一下，打不开文件了
road_theta_3 = np.array([
    45,225,135,90,180,135,180,300,270,300,30,70,20,110,20,20,315,45,225,45,195,225,135,315,225,315,45
])
theta_w_3 = np.radians(5) * np.ones(np.size(x3)) # 路、风夹角 
calculate_theta_w(theta_w_3,road_theta_3)

turn_index_3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
turn_theta_3 = [180,90,45,90,45,90,110,30,60,90,40,90,90,90,90,90,90,90,30,150,30,90,90,180,90,90]
turn_theta_3 = calculate_turn_theta(turn_theta_3)

height_3 = [1936,1948,1846,1821,1812,1712,1648,1587,1525,1620,2166,2205,2054,2898,1886,1682,1630,1783,1816,1823,1913,1907,1878,1844,1822,1842,1787,1906]
height_3 = calculate_height(height_3)
theta_3 = [0.3048 * calculate_theta(x3[i],height_3[i]) for i in range(len(x3))] 

Nd_4 = 6
N_turn_4 = 5 
x4 = [0,2.5,5,7.5,12.5,17.5,20] 
x4 = calculate_x(x4)
x4 = [x * 1 for x in x4]

wind_theta_4 = math.radians(wind_theta_dict["N"]) # 要改一下，打不开文件了
road_theta_4 = np.array([
    90,180,180,270,0,90 
])
theta_w_4 = np.radians(5) * np.ones(np.size(x4)) # 路、风夹角 
calculate_theta_w(theta_w_4,road_theta_4)

turn_index_4 = [0,1,2,3,5] 
turn_theta_4 = [90,180,180,270,90]
turn_theta_4 = calculate_turn_theta(turn_theta_4)

height_4 = [0,0,5,0,0,0,0]
height_4 = calculate_height(height_4)
theta_4 = [calculate_theta(x4[i],height_4[i]) for i in range(len(x4))] 


if __name__ == "__main__":
    print(len(x3))
    print(len(turn_index_3))
    print(len(turn_theta_3))