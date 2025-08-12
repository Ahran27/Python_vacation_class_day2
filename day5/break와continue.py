# while문의 처음 조건으로 이동한다.
# while에서 continue를 마나면 현재 반복을 건너뛰고 다음 조건을 다시 검사

count = 0
while count < 10:
    print(count)
    count += 1 # 여기까지는 평범한 while문
    if count == 5:
        break # 특정상황이나 예외상황에 즉시 멈춰야 할 때. while 조건에 만족해도 멈춤


num = 0
while num < 20:
    num += 1
    if num == 5: # 컨티누 만나는 순간 5를 입력하지 않고 다음부터 계속
        continue
    print(num,end=" ") # ,end=는 옆으로 진행하도록 하는것. " "는 공백


# while, if, coutinue를 사용하여  369게임 만들기
