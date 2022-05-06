# 파일 열기 모드 w:쓰기 / a : 추가 / r : 읽기

#파일 쓰기 = open("파일 이름", "파일 모드")
#파일 객체.write(데이터) , 파일객체.close()

#file = open("data.txt", "w")    #  w : 덮어쓰기 a : 이어쓰기
#file = write("파이썬 공부")
#file.close()

#file =open("data.txt", "r") # 읽기모드
#file = file.read() 

#with 구문 사용X 
#file=open("data.txt","r")
#data = file.read()
#file.close()

#with 구문 사용O
#with open("data.txt", "r") as file:
#    data = file.read()
