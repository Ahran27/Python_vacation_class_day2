#def 함수이름(매개변수)
#밥솥같은 것. 안에 넣는 재료에 따라 나오는 결과물이 달라짐
#개수 정해져있지 않음
def candy_fluff(count):
    print("오늘은 솜사탕을 " + str(count) + "개 만들어야 합니다")

candy_fluff(15)
candy_fluff(100)
candy_fluff(10)

def plus(a,b):
    print(a + b)

plus(10,20)


#매개변수 값 지정하기
def greet(name,greeting="안녕하세요"):
    print(f"{greeting},{name}!")

greet("영희")
greet("철수","반갑~")