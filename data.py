import numpy as np
import math
def angle(x):
    return float(np.radians(x))

x1 = [0.9,1.8-0.9,3.0-2.0,4.0-2.0,5.0-4.0,6.0-5.0,7.0-6.0,7.4-7.0,8.4-7.4,9.0-8.4,10.0-9.0,11.0-10.0,12.0-11.0,13.8-12.0,15.4-13.8,17.4-15.4,18.1-17.4,19.1-18.1,20-19.1,21.4-20\
    ,22.3-20,24.8-22.3,25.9-24.8,27-25.9]
height = [
    40-33,25-40,6-25,7-6,4-7,4-4,8-4,25-8,21-25,0-21,2-0,10-2,4-10,9-4,18-9,25-18,8-25,7-8,7+3,6+3,4+6,10-4,16-10,31-16
]

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
wind_theta = math.radians(wind_theta_dict["NNE"])
road_theta= np.array([
    70,225,180,270,180,150,210,330,
    225,250,220,180,180,225,0,340,60,135,140,230,240,0,230,180
]) # 路面与北方向的夹角
theta_w = np.radians(5) * np.ones(24) # 风与路面夹角数据，在下方进行处理

def calculate_theta(x,height): # 处理坡度的函数
    return math.atan(height * 0.3048 / (x * 1609.344))

def calculate_theta_w(theta_w,road_theta): # 处理风与道路夹角的函数
    # wind_theta: float, road_theta: list
    for i in range(np.size(road_theta)):
        theta_w[i] = math.radians(np.float(road_theta[i])) - wind_theta 
    
theta_1 = [
    calculate_theta(x1[i],height[i]) for i in range(len(x1))
] # 路面坡度数据
turn_index = [0,1,2,3,3,4,7,8,11,12,13,15,16,17,18,19,19] # 拐角对应的片段序号
turn_theta = [angle(120),angle(90),angle(90),angle(60),angle(90),angle(90),angle(80),angle(90),angle(70),angle(90),angle(60),angle(90),angle(60)\
    ,angle(90),angle(90),angle(90) ,angle(90)][::-1]
    # 转弯角度数据
calculate_theta_w(theta_w,road_theta) # 计算风和路面的夹角

x2 = [] 
x3 = [] 
x4 = []

if __name__ == "__main__":
    for p in theta_1:
        print(180 / math.pi * p)