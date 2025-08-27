class Person:
    def __init__(self):
        print("생성자가 호출됨!")

class Person2:
    def say_hello(self):
        print("안녕하세요!")#메서드. 생성자가 없어서 그냥 출력안됨

p1 = Person()

p2 = Person2()

p2.say_hello()#p2가 Person2클라스를 불러서 사용
