#1.import package 패키지.모듈   ==> setting.json 에 패키지 쪽 경로 추가 필요.

import unit.character

unit.character.test()

#2. from 패키지 import 모듈  **************8

from unit import item
item.test()

#3. import * ==> __init__ 수정
from unit import *   #*로 할떄는 __init__ 을 수정해줘야한다. 
item.test()
monster.test()
character.test() 

#4. import 패키지  --> init 모듈 수정 필요  ( from . import item, character, monster)
import unit
unit.character.test()

