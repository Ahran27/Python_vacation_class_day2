'''
붕어빵 클래스를 만든다.
생성자는 어떤맛인지, 개수
making이라는 메서드(***맛 붕어빵 **개 나왔습니다) 만들어
'''

class Boong:
    def __init__(self,flavor,count):
        self.flavor = flavor
        self.count = count

    def making(self):
        print(f"{self.flavor}맛 붕어빵 {self.count}개 나왔습니다.")

b1 = Boong("민초",5)
b2 = Boong("불닭",2)
b3 = Boong("초코",8)
#print(Boong)

b1.making()#위의 메서드 사용
b2.making()
b3.making()