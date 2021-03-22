def angle(v1, v2):
    dx1 = v1[2] - v1[0]
    dy1 = v1[3] - v1[1]
    dx2 = v2[2] - v2[0]
    dy2 = v2[3] - v2[1]
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180/math.pi)
    # print(angle1)
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180/math.pi)
    # print(angle2)
    if angle1*angle2 >= 0:
        included_angle = abs(angle1-angle2)
    else:
        included_angle = abs(angle1) + abs(angle2)
        if included_angle > 180:
            included_angle = 360 - included_angle
    return included_angle

import numpy as np
def angle3():
    x=np.array([0.9,-0.8,-0.7])
    y=np.array([3.4,0.1,3.4])
    # 两个向量
    Lx=np.sqrt(x.dot(x))
    Ly=np.sqrt(y.dot(y))
    #相当于勾股定理，求得斜线的长度
    cos_angle=x.dot(y)/(Lx*Ly)
    #求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度
    # print(cos_angle)
    # 弧度制
    angle=np.arccos(cos_angle)
    angle +=np.pi/18
    if angle > np.pi/2:
        angle = np.pi/2
    return angle

    # angle2=angle*360/2/np.pi
    # #变为角度
    # print(angle2)

# v1 = [0.9,-0.8,-0.7]
# v2 = [0.6,-2.6,0.5 ]
# v2 = [3.4,0.1,3.4]
# # =IFERROR(ANG(EMA!D$2:EMA!F$2,EMA!D3:EMA!F3)+0.174,1.6)=1
# a = angle(v1, v2)
# print(a)
# angle3()

import math

def Cosine(vec1, vec2) :
    result = InnerProduct(vec1,vec2) / (VectorSize(vec1) * VectorSize(vec2))
    return result

def VectorSize(vec) :
    return math.sqrt(sum(math.pow(v,2) for v in vec))

def InnerProduct(vec1, vec2) :
    return sum(v1*v2 for v1,v2 in zip(vec1,vec2))

def Euclidean(vec1, vec2) :
    return math.sqrt(sum(math.pow((v1-v2),2) for v1,v2 in zip(vec1, vec2)))

def Theta(vec1, vec2) :
    return math.acos(Cosine(vec1,vec2)) + math.radians(10)

def Triangle(vec1, vec2) :
    theta = math.radians(Theta(vec1,vec2))
    return (VectorSize(vec1) * VectorSize(vec2) * math.sin(theta)) / 2

def Magnitude_Difference(vec1, vec2) :
    return abs(VectorSize(vec1) - VectorSize(vec2))

def Sector(vec1, vec2) :
    ED = Euclidean(vec1, vec2)
    MD = Magnitude_Difference(vec1, vec2)
    theta = Theta(vec1, vec2)
    return math.pi * math.pow((ED+MD),2) * theta/360

def TS_SS(vec1, vec2) :
    return Triangle(vec1, vec2) * Sector(vec1, vec2)

# vec2 = [1.4,2.7]
# vec1 = [1.11 ,2]
# # 1.11,2,11 
# # 

# print('tx',TS_SS(vec1,vec2)*np.pi)


# =IF(G3<=1.6,(EMA!G$2*EMA!G3*ABS(SIN(G3))*G3*(H3+ABS(EMA!G$2-EMA!G3))^2)/4,(EMA!G$2*EMA!G3*ABS(SIN(1.6))*1.6*(H3+ABS(EMA!G$2-EMA!G3))^2)/4)

g2 = 1.38953891236108
g3 = 2.65739782810312

angle = 1.11 # 夹角
h3 = 2.51  # 欧几里得长度
r = 11
if angle < (np.pi/2):
    r = g2 * g3 * abs(math.sin(math.degrees(g3))) * g3 *(h3 + abs(g2 - g3)**2)
    r = r / 4
else:
    r = g2 * g3 * abs(math.sin(math.degrees(g3))) * (np.pi / 2) * (h3 + abs(g2 -g3)**2)
    r = r / 4
print(r)
