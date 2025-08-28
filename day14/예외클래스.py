#age = int(input("나이를 입력해주세요: "))
#print(f"저의 나이는 {age}살입니다.")

try:
    age = int(input("나이를 입력해주세요: "))
    if(age < 0 or age > 150):
        raise Exception("나이는 0 이상 150 이하로 작성하세요.")
except Exception as e:
    print(e)
else: print(f"당신은 {age}살이군요!")
finally:#클래스 끝날 때의 유언
    print("프로그램을 종료합니다.")

    """
    class 클래스 이름(부모클래스):
        def __init__(self):
        super().__init__("예외메세지"):
    """

class AgeError(Exception):
    def __init__(self):
        super().__init__("사람의 나이는 0살이상, 150미만으로 작성할 것")
try:
    age = int(input("나이를 입력하세요: "))
    if (age < 0 or age > 150):
        raise AgeError
except AgeError as e:
    print(e)
else:
    print(f"당신은 {age}살이군요!")
finally:#클래스 끝날 때의 유언
    print("프로그램을 종료합니다.")
