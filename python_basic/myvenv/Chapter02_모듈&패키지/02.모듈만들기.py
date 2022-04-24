import pay_module    #만든 모듈의 경우 파일 경로를 생각하여 파일을 생성 하거나, 경로를 지정해줘야 함
#file -> preference -> setting.json 에   "python.analysis.extraPaths": ["./myvenv/Chapter02_모듈&패키지"]    추가 해서 모듈을 불러 올 수 있도록 함

print(pay_module.version)

pay_module.printAuthor()
pay_info = pay_module.Pay("20220424", 20000,"2022-04-24")

print(pay_info.get_pay_info()) 
print(pay_module.__name__)



