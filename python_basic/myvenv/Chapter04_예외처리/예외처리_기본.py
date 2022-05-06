#try - catch  구문 

#try:
#    예외가 발생 할 수 있는 코드
#    
#excpet:
#    예외가 발생시 실행할 코드
#
#else:
#    예외가 발생X 경우 실행할 코드
#
#finally:
#    항상 d실행할 코드


#원화를 입력받고 환율을 입력 받음 -> 원화를 달러로 변환하여 출력

won = input("원화금액 입력 : ")
dollar = input("환율 입력 하세요 :")

#print(int(won) / int(dollar))#둘다 문자열 이니까 int로 변환하여 계산

# 숫자 대신 문자 입력 할 시 오류 발생 (valueError 발생) ==> 예외
# 나누기 0 ==> zeroDivisionError 발생 ==>예외
# 예외가 발생하는 부분을 try 에 넣도록!!
try:
    print(int(won) / int(dollar))#둘다 문자열 이니까 int로 변환하여 계산

except ValueError as e:  # 예외 발생 시 지정하여 예외처리 할 수 있음.
    print("문자열 말고 숫자 써줘!" , e)# as e -->예외 메세지 출력해줌
except ZeroDivisionError as e: # 0으로 나눌시
    print("나누기 0 은 불가능해!", e)
except:
    print("예외가 발생했습니다. ") 
else:
    print("예외 없음")