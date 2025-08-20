"""
딕셔너리처럼 순서가 없음. --> 인덱스 사용 불가
근데 좀 특별한게 중복된 값을 허용하지 않음(집합개념과 비슷). 서로 다름 값 모아서 정리.
같은 값 여러번 저장해도 1개로 저장
변수명 = {요소1, 요소2, 요소3}
"""
'''
❗❗리스트 : []

❗❗딕셔너리 : {
키:값
}

❗❗튜플 : ()

❗❗세트: {}
--> {}를 사용하는 애들은 인덱스 쓸 수 없음❗❗
'''

str = "apple"
list = [1,2,3]
tuple = (1,2,3)

set_str = set(str)
set_list = set(list)
set_tuple = set(tuple)
print("set_str: ",set_str) #순서 없는 자료이기 때문에 {'p','a','l','e'}이렇게 나옴
print("set_list: ",set_list)
print("set_tuple: ",set_tuple)

