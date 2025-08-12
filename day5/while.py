# 반복문
count = 0
while count < 100: # 조건이 참인지 검사
    print(count) # 참이라면 괄호 안의 것을 반복해라
    #count = count + 1
    count += 1 # 복합대입 연산자 사용 점점 늘어나게. 변수가 더해지다가 조건과 같거나 커지면 종료

#10부터 5까지 감소하는
gamso = 10
while gamso >= 5:
    print(gamso)
    gamso -= 1 # 복합 연산자를 프린트보다 먼저 쓰게 되면 작용하지 않음. 먼저 하면 감소 부터 하고 프린트 되기 때문에

'''
 우리가 가진 돈 : 5000
아이스크림: 1000
아이스크림을 2번 사먹을 것
아이스크림을 1번 사먹었다! 남은 돈 : ???
아이스크림을 2번 사먹었다! 남은 돈 : ???
'''
'''
내 답
budget = 5000
count = 0
while budget >= 3000:
    print("아이스크림을",count,"번 사먹었습니다. 남은 돈은 ",budget,"입니다.")
    count += 1
    budget -=1000
'''
#선생님 답
money = 5000
icecream_price = 1000
icecream_count = 1

while icecream_count <=2:
    money -= icecream_price
    print(f"아이스크림을{icecream_count}번 사먹었다! 남은 돈은 {money}원.")
    icecream_count += 1

    num = 0 #사용자 입력프로그램 대기하는 프로그램 같은거. 예외가 생기기 전까지 움직임. 심심이 같은 것
    while num <3:
        print(num)