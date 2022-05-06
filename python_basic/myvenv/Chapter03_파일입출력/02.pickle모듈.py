#파이썬 객체를 pickle로 저장하기
import pickle    #내장 (객체를 저장 파일 입출력 관련 모듈)

data = {
    "목표1" : "매일 공부 1시간",
    "목표2" : "매일 운동 30분"
}

file = open("./myvenv/Chapter03_파일입출력/data.pickle", "wb")  # write binary
pickle.dump(data, file)
file.close()

file = open("./myvenv/Chapter03_파일입출력/data.pickle", "rb") #read binary
data = pickle.load(file)
print(data)
file.close()

with open('data.txt', 'r', encoding='utf8') as file :
    data = file.read()
    #file.close() 자동으로 해줌 =>with 구문이라. 

