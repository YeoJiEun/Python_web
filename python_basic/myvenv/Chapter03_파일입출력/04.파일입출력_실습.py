import csv

path = './myvenv/Chapter03_파일입출력/'
# 주식 파일 생성
data = [
    ['종목', '매입가', '수량','목표가'],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER" , 380000, 5 ,400000]
]

file = open(path+"mystock.csv", "w", newline="",encoding='utf-8-sig')
# file.write(data)  # ******틀렸음 writer = csv.writer(file)
writer = csv.writer(file)
for d in data:   #*************
    writer.writerow(d)   #****************
file.close()

#수익금 = (목표가 - 매입가) * 수량
#수익률 = (목표가/매입가 - 1) * 100

def show_info(data):
    for a in data[1:]:
        a = int(a)
        
    suik_1 = (data[3] - data[1]) * data[2]
    suik_2 = (data[3]/data[1] - 1) * 100
    
    print(f"{data[0]} {suik_1} {suik_2:.2f}% ")  # :.2f - 소수점 2재짜리 까지 출력

with open(path+"mystock.csv", "r", encoding="utf-8-sig") as file:
    reader = list(csv.reader(file))  #리스트 형 아니어서, 리스트로 변환해줘야 [1:] 이런식의 연산이가능 
    for d in reader[1:]:
        d[1] = int(d[1])
        d[2] = int(d[2])
        d[3] = int(d[3])
        a = []
        a.append(d[0])
        suik_1 = (d[3] - d[1]) * d[2]
        suik_2 = (d[3]/d[1] - 1) * 100
        a.append(suik_1)
        a.append(suik_2)

        print(a) # 이런 식으로 말고 클래스 및 함수 를 활용하자 !

    for d in reader[1:]:
        show_info(d)

