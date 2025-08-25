'''
실행함수
x,y,연산자(operation)받을 것

행동함수
더하기 함수
마이너스 함수
곱하기 합수
나누기(몫)함수
'''

def calculation(x,y,operation):
    return operation(x,y)
    # e.g. plus(2,3)

def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiple(x,y):
    return x * y

def divide(x,y):
    return x // y

plus_result = calculation(2,3,plus)
print(plus_result)
minus_result = calculation(2,3,minus)
print(minus_result)
multiple_result = calculation(2,3,multiple)
print(multiple_result)
divide_result = calculation(2,3,divide)
print(divide_result)