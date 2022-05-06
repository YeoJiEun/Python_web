#csv = 데이터가 콤마로 구분된 텍스트파일 형식 ex) 이름,반,번호,성별 등.. (excel)

import csv

data = [
    ['이름','반','번호']
    ,["지은",8,30]
    ,["지현",8,31]
    ,["남희",7,32]
]
file = open("./myvenv/Chapter03_파일입출력/student.csv","w", newline="",encoding="utf-8-sig")  # newline="", encoding="utf..."window 는 생성시 한줄 씩 띄어지기 때문에 붙여줘야 붙여서 나옴
writer=csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()


#csv 파일 읽기 
file = open("./myvenv/Chapter03_파일입출력/student.csv","r",encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)


file.close()

