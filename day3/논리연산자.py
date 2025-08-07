#참거짓 판단 연산자
'''
1. and(&&) : 연산자를 기준으로 왼쪽과 오른 쪽 값이 모두 true일 때만 ture를 반환. 하나라도 아닐시 false
2. or(||) : 연산자를 기준을 왼쪽과 오른쪽 값 중 하나라도 ture가 있으면 true를 반환. shift + 원화표시
   ㄴ  둘 다 false라면 false를 반환
3. not()! : 뒤에 따라오는 논리값이 true aus  false를 반환(반대로 출력됨)
'''

num1 = 10
num2 = 20
num3 = 30

num_result = num1 < num2 and num2 > num3
num_result2 = num1 > num2 or num3 > num2
print(num_result2)

false = False
print(false)
print(not false)

username = ""
result = not username
print("username에 값이 비어 있나요?",result)

number = 15
#15라는 숫자가 10과 20 사이에 있는지 확인하고 싶음
#있다면 true  /  없다면 false

result = 10 <= number <= 20
print(result)

current = int(input("현재 경험치를 입력하세요: "))
target = 1500
print("레벨업까지 남은 경험치: ",target - current)
