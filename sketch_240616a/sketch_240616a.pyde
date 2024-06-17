import csv
f = open('./data/output_file.csv','r')

rdr = csv.reader(f)
rdr = list(rdr)[-1]
data = rdr[0].split()
WD = int(data[2]) # 풍향
WS = int(float(data[3])) # 풍속
PA = data[7].replace('.', '')[2:5] # 기압
TA = data[11] # 기온
CA_TOT = data[25] # 전운량
TD = data[12] # 이슬점 온도
WW = data[24] # 국내식 일기 코드
print(WD,WS,PA,TA,CA_TOT,TD,WW)

def setup():
    size(500,500)
    
def draw():
    # 막대
    pushMatrix()
    translate(250, 250)
    rotate(radians(WD))
    line(0, 0, 0, -150)
    for i in range(0, (WS//5)):
        y = -150 + (i * 10)
        line(0, y, 50, y)
    for i in range(0, WS - (WS//5 * 5), 2):
        y = -150 + ((WS//5) * 10) + (i * 10)
        line(0, y, 25, y)
    popMatrix()
    # 운량
    # 원래 작업 해야함
    fill(0, 0, 0)
    circle(250,250, 50)
    # 기압 나타내기
    fill(0, 0, 0)
    textSize(20)
    text(PA, 280, 260)
    # 기온 나타내기
    fill(0, 0, 0)
    textSize(20)
    text(TA, 180, 230)
    # 일기 나타내기
    # 원래는 도형으로 만들어야함
    fill(0, 0, 0)
    textSize(20)
    text(WW, 180, 250)
    # 이슬점 나타내기
    fill(0, 0, 0)
    textSize(20)
    text(TD, 180, 280)
