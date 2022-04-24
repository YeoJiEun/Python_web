#결재 정보, 관리 모듈

version = 2.0

#함수
def printAuthor():
    print('코딩 start')

#클래스
class Pay:
    def __init__(self, id, price, time):
        self.id  =id;
        self.price = price
        self.time = time
    
    def get_pay_info(self):
        return f" 카드정보 {self.id}, {self.price}, {self.time} 입니다. "

if __name__ == "__main__": #이 모듈을 자기자신이 직접 실행했을 떄만 실행된다. 
    print("여기서 실행")

