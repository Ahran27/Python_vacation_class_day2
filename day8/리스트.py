"""
가장 많이 사용되는 자료 구조
여러개의 값을 하나의 변수에 한번에 저장하는 것.
일상의 목록과 같은 개념
다른 언어에서는 '배열'
"""
num = 7
nums =[0,1,2,3] # 리스트. 숫자, 문자, 논리값 등 넣을 수 있음

alphabets = ['a','b','c'] # 문자
boolean_type = [True,False,True] # 논리
greetings = ["hello","오늘은 파이썬","8일째"]

#index: 각 리스트의 위치를 나타내는 번호. 0부터 시작
mixed_list = [1,"apple",3.14,True]
print(mixed_list)

mixed_list[0] = 2 # 0번자리에 있는 것을 2로 바꾸라
print(mixed_list)

mixed_list[1] = "망고"   # 1번자리에 있는 것을 망고로 바꾸라
print(mixed_list)

family = ["mother","father","sister","dog"]
print(family[-1]) # 마지막거

'''
list[start:end:step]
'''

numbers = [10,20,30,40,50]
print(numbers[0:3])#원하는 자리의 다음 번호로 쓰기 0~2를 원하명 3

print(numbers[-2:])# 마지막까지 하려면 end는 생략

print(numbers[::2])# 시작부터 2씩 뛰며

#numbers[0] = 100
#numbers[1] = 200
#print(numbers)

numbers [:2] = [100,200] # 위의 주석을 간단하게 한번에 하려면 이렇게
print(numbers)

numbers[:2] = [] #1자리까지 비워짐
print(numbers)

