
def seat(x,y):
    return x/0.414+(y-6)/1.414

# 스피커 위치 좌석 기준으로 변환
x11 = 0
x21 = 15
y11 = seat(x11, y11)
y21 = y12

# 파장, 파수 좌석 기준 변환
def l(x,y):
    return abs((x-(y-7))/1.414)

ld0 = ((l(x11,y11)+ld)**2-l(x11,y11)**2)**0.5
ld2 = ((l(x31,y31)+ld)**2-l(x31,y31)**2)**0.5
ld4 = ((l(x51,y51)+ld)**2-l(x51,y51)**2)**0.5
ld6 = ((l(x71,y71)+ld)**2-l(x71,y71)**2)**0.5

k0 = 2*np.pi/ld1
k2 = 2*np.pi/ld3
k4 = 2*np.pi/ld5
k6 = 2*np.pi/ld7

