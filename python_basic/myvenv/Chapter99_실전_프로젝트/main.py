import csv as c

class post:
    num = 0
    def __init__(self, title, content):
        
        self.title = title
        self.content = content


select = 99
while(select != '3'):


    print(f'''- 메뉴를 선택해 주세요 - 
    1. 게시글 쓰기
    2. 게시글 목록
    3. 프로그램 종료
    ''')

    try:
        select = input()
        if(select != '1' and select != '2' and select != '3'):
            raise Exception
    except:
        print("1 / 2 / 3 으로만 입력 해주세요")

    if(select  == '1'):
        title = input("제목을 입력해주세요 >>> ")
        content = input("본문 입력해주세요 >>> ")
        post(title, content)
        print("게시글이 등록되었습니다.\n")
    
