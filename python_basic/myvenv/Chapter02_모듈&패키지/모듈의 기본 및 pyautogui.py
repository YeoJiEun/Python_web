#모듈을 쓰는 이유 : 기능별로 나누어 관리 = 유지보수 및 관리 용이
#모듈 사용법
#import 모듈 명(math)
#모듈명.변수 , 모듈명.함수()
# ex) print(math.ceil(5.7)) 올림 적용

import math #from math import pi,ceil 라고 써도 가능 ==> 이렇게하면 math. 안붙여도 됨.
#from math import pi, ceil as c  ==> c라는 별칭 붙여서 c(2.7) 이런식으로 이용가능
print(math.pi)
print(math.ceil(2.7))

#파이썬 외부모듈 (다른 이가 만든 모듈)
#pip install 모듈이름 

# pyautogui 매크로 설치 (마우스 키보드 제어!) 구글링하면 레퍼런스확인 가능
import pyautogui as pg
import time
import pyperclip #한글 입력시 필요한 모듈
pg.moveTo(500,500,duration=2)
#x 500 y 500 위치에 2초동안 마우스 이동 

time.sleep(1)
print(pg.position()) #1초뒤 마우스 현재위치 확인
# x=1061, y=118    ~   x=1894, y=550 

pg.moveTo(1061, 118)
pg.moveTo(1894, 550, 2) #2초동안 이 위치로 이동
# 마우스 이동 

pg.click()
pg.click(button='right')
pg.doubleClick()
pg.click(clicks=3, interval=1) # 3번 클릭을 1초마다
# 클릭 관련 

pg.moveTo(1061, 118, 1)
pg.dragTo(1894, 550, 2)
# 드래그

pg.write('hello.world!') #타이핑 interval=0.25 ==> 0.25마다 타이핑함
pg.press('left', presses = 3) #왼쪽키 3번 입력

pg.hotkey('ctrl','c') #ctrl+c 동시 입력 
pyperclip.copy('캡처') #클립보드에 텍스트 복사하여 출력



#로그검토대장 자동화에 이용해보는 프로그램 만들어보기.(4/30까지)
