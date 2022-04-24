#정책검토를 위해 보안솔루션 정책 화면을 캡처하는 과정을 자동화하는 것을 목표로 함 
import pyautogui as pg
import time
import pyperclip #한글 입력시 필요한 모듈
print(pg.size()) # 현재 모니터 사이즈 출력
#삼성 노트북 : Size(width=1920, height=1080)

time.sleep(1)
print(pg.position()) #1초뒤 마우스 현재위치 확인
# 791 1057


#616 368

#캡처범위 1026 198   -  1676 520
pyperclip.copy('캡처')
pg.press('win') #pg.click(795,1057)

pg.hotkey('ctrl','v')
pg.press('enter')
time.sleep(0.5)
pg.hotkey('ctrl', 'n') # 새캡처 버튼
pg.moveTo(1026,198)
pg.click()
pg.dragTo(1676, 520, 1)
time.sleep(1)
pg.hotkey('ctrl','c')
pg.press('win')
pg.write('powerpoint')
pg.press('enter')
pg.hotkey('ctrl','v')
