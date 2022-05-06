file = open("./myvenv/Chapter03_파일입출력/data.txt", "w" , encoding='utf8')   #경로는 root 디렉토리부터 시작, 폰트 깨지면 encoding 적용 
file.write("파이썬 시작")
file.close()

#파일에 이어서 쓰기
file = open("./myvenv/Chapter03_파일입출력/data.txt","a", encoding="utf8")
file.write(" \n이어붙여서 넣기")
file.close()

file = open("./myvenv/Chapter03_파일입출력/data.txt", "r", encoding='utf8')

data = file.read()
print(data)
#file.close()

# 파일 한 줄 읽기
while True:
    data = file.readline() # 한줄 읽기
    print(data)
    if data == '':
        break
file.close()

