"""
상속이란
부모클래스(수퍼클래스)의 속성과 메서드를 물려받아 사용할 수 있도록 만드는 개념

"""

class Animal:#슈퍼클래스
    def __init__(self,type):
        self.type = type

    def make_sound(self):
        print("소리를 냅니다~")

class Dog(Animal):#슈퍼클래스 이름을 가져옴
    def __init__(self,name,breed):
        super().__init__("갱얼쥐")
        #부모클래스의 생성자를 불러서 self.type = "갱얼쥐"
        #super() 부모 클래스의 속성과 기능을 가져다 쓰겠다!
        #그런데 가져다 쓰려고 보니 type을 설정하는 코드가 있다? 가져다 써야쥐

        self.name = name
        self.breed = breed

    def make_sound(self):
        print("멈멍 ㅗ알아ㅘㄹ")
        #오버라이딩(재정의)
        #부모클래스에서 정의한 메서드를 자식클래스가 다시 정의하는 것
        # 부모 것도 있는데 난 내가 바꿔서 쓸래

dog = Dog("개개","아프간하운드")
print(f"{dog.name}는 {dog.breed}이며, {dog.type}입니다.")
#________________________________________________________
class Cat(Animal):#슈퍼클래스 이름을 가져옴
    def __init__(self,name,breed):
        super().__init__("냥이")
        #부모클래스의 생성자를 불러서 self.type = "갱얼쥐"
        #super() 부모 클래스의 속성과 기능을 가져다 쓰겠다!
        #그런데 가져다 쓰려고 보니 type을 설정하는 코드가 있다? 가져다 써야쥐

        self.name = name
        self.breed = breed

    def make_sound(self):
        print("먀아 ㅗ알아ㅘㄹ")

cat = Cat("캣캣","삼색이")
print(f"{cat.name}는 {cat.breed}이며, {cat.type}입니다.")