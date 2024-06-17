import csv
 
f = open('output_file.csv','r')
rdr = csv.reader(f)

rdr = list(rdr)[-1]
data = rdr[0].split()

WD = data[2]
WS = data[3]
PA = data[7]
TA = data[11]
CA_TOT = data[25]
TD = data[12]
WW = data[24]

print("풍향 (16방위): ", WD)
print("풍속 (m/s): ", WS)
print("현지기압 (hPa): ", PA)
print("기온 (C): ", TA)
print("전운량 (1/10): ", CA_TOT)
print("이슬점 온도 (C): ", TD)
print("국내식 일기코드 (문자열 22개): ", WW)

f.close()