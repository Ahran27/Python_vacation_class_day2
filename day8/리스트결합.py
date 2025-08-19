#여러리스트를 결합해 하나의 리스트로 만듬

list1 = ['a','b','c']
list2 = ['d','e']

list3 = list1 + list2 # 기존리스트 변경 없음
print(list3)

list1.extend(list2) #또 다른 방법의 결합. 리스트의 원본이 변경됨
print(list1)

list4 = list2 * 3 # 리스트2의 3번 반복
print(list4)

print("리스트의 길이 확인")
result = len(list4) #list4에 6개가 들어있다
print(result)

print("리스트에서 특정 값이 있는지 확인")
print('d' in list4) #참거짓으로 d가 있는지 확인

#리스트에서 특정 값의 개수 구하기 (e)
result2 = list4.count('e')
print(result2)

print("리스트의 최대값, 최소값 구하기")
list5 = [1,2,3,4,5]
print(max(list5))
print(min(list5))