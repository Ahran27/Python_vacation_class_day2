'''
다른데에서 함수 가져와서 쓰기
방법
    1. import 파일이름
    2. from 파일이름 import 변수, 함수, 클래스
    3. from 파일이름 import *
'''
#from day14.hello import my_name
#import hello#가져오겠다 선언.소규모일때 추천      1번방법
#from hello import self_pr
#from hello import my_name.파일 클 때 추천      2번방법
#hello.self_pr()#가져오기
#self_pr()
#my_name("babo")
#print(hello.water)#hello라는 파일에서 water라는 변수 가져오기

#hello.my_name("아란")#hello라는 파일에서 my_name라는 함수 가져오기

from hello import *#3번방법. 선언이 맨 위에 있고 줄이 길면 어디서왔는지 모르고 지저분해서 비추.
self_pr()
my_name("idiot")
print(water)