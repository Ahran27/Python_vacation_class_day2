def greet(name):
    print(f"안녕하세요 {name}님!")

greet("민수")

def callback_function(callback):
    print("이제 콜백함수 실행할거임")
    callback("이수근")

callback_function(greet)


#---------------------------------------------
def hello(name):
    print(f"안녕{name}!")

hello("봄")

def hello_callback(callback,name):
    # callback: 실행할 다른 함수를 넣어주는 공간.(이름을 임의로 정해줌)
    # name: 이름을 받을 것
    callback(name)#hello(name)

hello_callback(hello,"아란")

#---------------------------------------------
def dinner(name):
    print(f"{name}님은 저녁을 먹었습니다.")

def lunch(name):
    print(f"{name}님은 점심을 먹었습니다.")

def eating(eat,name):
    eat(name)
    # 밥을 먹는 함수
    #dinner(name)

eating(dinner,"아란")
eating(lunch,"아란")