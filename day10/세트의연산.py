'''
a = {2,3,6}
b = {3,6,9}
교집합은 3,6.이런걸 계산하기 위해 세트 사용

& 연산자 사용
intersection()
'''

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a)
print(set_b)

intersection_AandB = set_a.intersection(set_b)#두 세트의 교집합을 찾아달라
print(intersection_AandB)

and_AandB = set_a & set_b#두 세트의 교집합을 찾아달라. 근데 새 세트 생성
print(and_AandB)

'''
과일을 구매했다!
딸기, 오렌지, 체리
내가 좋아하는 과일 : 포도, 오렌지, 딸기
'''

set_fruits = {"딸기", "오렌지","체리"}
set_favorites = {"포도", "오렌지", "딸기"}

and_fruits = set_fruits & set_favorites
print(and_fruits)


set_a_2 = {1,2,3,4}
set_b_2 = {3,4,5,6}

'''
#❗❗합집합. 두개의 원소를 모두 합한 것. 중복된 요소 한번만
| : 파이프연산자. shift + 원화 표시
union()
'''

union_set = set_a_2 | set_b_2
print(union_set)

union_set2 = set_a_2.union(set_b_2)
print(union_set2)
'''
#❗❗차집합. a에 속하지만 b에 속하지 않는 요소
- : 마이너스 연산자
difference()
'''
set_a_3 = {1,2,3,4}
set_b_3 = {3,4,5,6}

diff_set = set_a_3.difference(set_b_3)
print(diff_set)

minus_set = set_a_3 - set_b_3
print(minus_set)

'''
add(): 한 번에 하나의 요소 추가
update(): 여러개의 요소를 한꺼번에 추가
'''

set_method = {1,2,3}
set_method.add(4)
print(set_method)

set_method.update({5,6})
print(set_method)

'''
remove(): 특정 요소 제거(요소가 없으면 오류남)
discard(): 특정 요소 제거(요소가 없어도 에러가 나지 않음)
pop(): 임의의 요소를 제거하고 반환
clear(): 모든 요소 제거
'''

set_c = {'a','g','t','f','e','h','y','p'}
set_c.remove('a')
print(set_c)
# set_c.remove("puppy")

set_c.discard("kitty")
print(set_c)

set_red = {'r','e','d'}
print(set_red)
print(set_red.pop())#임의의 요소제거기 때메 괄호 안에 안넣음
print(set_red)

set_red.clear()
print(set_red)