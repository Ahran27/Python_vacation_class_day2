a = "apple"
first_char = a[0]
third_char = a[3]
print(first_char)
print(third_char)

#마이너스 인덱스. 문자열의 뒷부분부터 시작하는 것. e.g apple의 e는 -1

last_char = a[-1]
print(last_char)
second_char = a[-4]
print(second_char)

#문자역 슬라이싱
#변수명[start:stop:step] : 문자열 술라이스 구조
'''
start: 슬라이싱을 시작할 위치를 정한다. (생략하면0!)
stop: 슬라이싱을 종료할 위치를 정한다. (*출력하고 싶은 단어의 마지막 인덱스 번호 + 1을 하여 작성)
step: 증감폭(인덱스의 증가 또는 감소 지정, 기본값 1, 생략하면 1)
'''

text = "I love pasta"
slicing1 = text[2:6]
print(slicing1)
slicing2 = text[7:12]
print(slicing2)
#인덱스 번호 더하기 일을 하는 이유는 마지막 인덱스번호의 전까지로 간주하기 때문에 +1을 해서 뒤까지 포함하는 것

slicing_step = text[7:12:2]
print(slicing_step)
#두번 건너뛰도록 하는 것

first_lost = text[:6]
print(first_lost)
#생략했으니 맨앞부터 나오는 것

last_lost = text[6:]
print(last_lost)
