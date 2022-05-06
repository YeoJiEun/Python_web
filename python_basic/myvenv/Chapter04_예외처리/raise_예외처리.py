#aise Exception
#raise Exception("에러 메세지")#필요시 메세지 나오도록

#Exception ==> 모든 내장 예외 가지고있음. ==> 특정 예외를 알 경우는 특정 예외만 지정해서 처리하는 것이 GOOD

#class 예외(Exception): #예외를 발생시킴 
#    def __init__(self): #Exception 상속
#        super().init("에러메세지")


#raise 구문 사용해서 예외 발생시키기.

try:
    num = int(input("음수 입력 : "))
    if(num >= 0):
        raise Exception("양수 입력 불가 !!!")

except Exception as e:
    print("에러 발생", e)
    

