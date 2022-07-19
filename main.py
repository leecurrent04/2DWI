import matplotlib.pyplot as plt
import numpy as np

# 진동수
frequency=1

# 위상차
phase = 1

# 시간 축
timeArray=np.linspace(0,8,10*8)
print(timeArray)

def drawGraph(distanceFromO,time):
    if time > 0:
        # v=hf (h=1로 가정)
        # r=vt
        radius = frequency * time
        x=np.linspace(-radius,radius,1000)

        y=[]
        for i in x:
            # 반 원에서의 y 좌표
            y.append(np.sqrt(radius**2-i**2))

        plt.plot(x+distanceFromO,y,c="r")


for t in timeArray:
    # Graph 크기
    plt.figure(figsize=(20,12))
    
    # 5개의 파원에 각 위상차를 적용한다.
    drawGraph(4, t+phase*2)
    drawGraph(2, t+phase*1)
    drawGraph(0, t+phase*0)
    drawGraph(-2, t-phase*1)
    drawGraph(-4, t-phase*2)

    # 파원 점 찍기
    plt.scatter([4,2,0,-2,-4],[0,0,0,0,0],c='blue')

    # Graph 범위
    plt.xticks(range(-16,17),range(-16,17))
    plt.yticks(range(0,17),range(0,17))

    #plt.show()
    plt.savefig("./data/%01.5f.png"%t)
    