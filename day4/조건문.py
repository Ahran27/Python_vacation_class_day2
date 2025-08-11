a = 7
b = 3

if a  > b:
    print("a가 b보다 큽니다.")

    if a < b:
        print("a가 b보다 큽니다.")

age = 20
if age >= 20:  # 단순 if. 조건이 충족되지 않을 경우, 출력되지 않음
    print("성인입니다.")

fruit = "apple"
if fruit == "banana":
    print("저는 바나나를 좋아해요")
else:
    print("not really...")

num = -3
if num >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")

#49가 7의 배수인지 확인하는 if 문 작성
number = 49
if number % 7 == 0:
    print("7의 배수입니다.")
else:
    print("7의 배수가 아닙니다.")


#elif 조건이 여러개
zero = 0
if zero > 0:
    print("0보다 큰 양수지롱")
elif zero == 0:
    print("o입니다")
else:
    print("음수다")