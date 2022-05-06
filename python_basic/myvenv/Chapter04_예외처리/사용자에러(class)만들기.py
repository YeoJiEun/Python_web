class PositiveNumError(Exception) : #새로운 에러 만들기
    def __init__(self):
        super().__init__("양수는 입력 불가")

try:
    num = int(input("음수 입력 : "))
    if(num >= 0):
        raise PositiveNumError

except PositiveNumError as e:
    print("에러 발생", e)
    