#딕셔너리는 키(사전)와 값으로 나눠짐
#키 : 값
#apple : 사과
#순서가 있는 구조가 아니라 인덱스 번호가 없음. 대신 키값으로 접근 가능
#대괄호 안에 인덱스 번호가 아니라 키값 넣어줌 .e.g.print(me["age"])

me = {
    "name" : "ahran",
    "age" : 25,
    "number" : "010-1234-5678",
    "class" : ["c언어", "파이썬", "java"]
}

tv= {
    "name" : ",삼성전자 fullHD",
    "colour" : "black",
    "inch" : "40"
}

print(me)
print(me["age"])

#친구목록
friends = {}
friends["도현"] = 19
friends["현종"] = 28
friends["현민"] = 32

print(friends)
#수정하기
friends["현민"] = 31
print(friends["현민"])
#삭제del
del friends["현종"]
print(friends)
#초기화
friends.clear()
print(friends)

'''
keys(): 딕셔너리의 모든 키를 뽑아 반환
values(): 딕셔너리의 모든 값을 반환
items(): 딕셔너리의 모든 키와 값의 쌍을 반환
update(other_dict): 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씀
'''

my_dict = {
    "name" : "kelly",
    "age" : 18,
    "city" : "New York"
}
keys = my_dict.keys()#리스트는 아니지만 리스트 처럼 보임
print(keys)

values = list(my_dict.keys())
print(values)

values = list(my_dict.values())
print(values)

items = my_dict.items()
print(items)

items = list(my_dict.items())
print(items)

my_dict.update({"age":21, "hobby":"swimming"})#딕셔너리 추가하기
print(my_dict)
#update: 키가 있다면 값을 변경 / 키가 없다면 추가

print(sorted(my_dict))
print(sorted(my_dict.items()))

print(sorted(my_dict, reverse=True))#내림차순 출력
