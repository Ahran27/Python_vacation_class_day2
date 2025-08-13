# 월-목 1-2교시
'''
1일차 1교시입니다.
1일차 2교시입니다.
'
'
로 나오게 출력
'''
day = 1
while day <= 4:
    lecture = 1
    while lecture <= 2:
        print("{}일차 {}교시 입니다".format(day,lecture))
        lecture += 1
    day += 1