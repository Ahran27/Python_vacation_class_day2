for num_list in [1,2,3,4,5]: #for 넘리스트(for문의 이름) 안에 1,2,3,4,5
    print(num_list)

a = [6,7,8,9,10]
for a_list in a:
    print(a_list)

for num_list in ["가","나","다"]:
    print(num_list)

#안녕하세요 블랙핑크 제니입니다.
blackpink = ["제니","로제","리사","지수"]
for hi_blackpink in blackpink:
    print(f"안녕하세요 블핑 {hi_blackpink}입니다.")

for char in "apple": # 문자열을 쪼개서 하나하나 출력됨. in 뒤에 있는 요소들을 하나하나 출력하기 때문에
    print(char)

#1~5 정수의 합
sum = 1+2+3+4+5 # 비효율적
'''
range(start, stop, step):
start: (선택적)시작 숫자(생략하면 기본값은 0)
stop: 숫자 범위의 끝(stop에 사용된 값은 포함하지 않음. e.g. stop에 5를 넣으면 4까지만
step: (선택적) 숫자를 증가시키는 간격 (생략하면 1)
'''
for range_for in range(5): #0~4
    print(range_for)

for range_for2 in range(2,6):
    print(range_for2)

for range_For3 in range(1,10,2): #1부터 9까지 2씩 건너뛰며->홀수만 출력
    print(range_For3)

for range_for4 in range(10,0,-2):
    print(range_for4)

#1~5까지의 합 구하기! 합계: ***
total = 0
for range_for5 in range(1,6):
    total += range_for5
print("합계: ",total) # 프린트가 for문 안에 들어가 있으면 합계가 여러개 나옴. for 문 바깥에 있어야 함

fruits = ["apple","banana","cherry"]
for fruits_list in range(len(fruits)): # len은 fruits에 들어있는 길이 // fruits를 넣어준 것은 range(3)이라고 생각하면됨. 실질적으로 2까지
    print(f"인덱스{fruits_list}: {fruits[fruits_list]}")

#range 사용하여 구구단 2단 출력

for num_multi in range(1,10):
    print (f"2 X {num_multi} = {num_multi*2}")