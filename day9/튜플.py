# 튜플: 리스트와 유사. 불변의 특징. 순서가 있는 데이터
# 한번 생성된 후에 요소의 값을 변경하거나 삭제할 수 없다
# 변수명 = (요소1, 요소2, 요소3)
# 고유한 인덱스번호로 접근 가능

colours = ["red","green","blue"]
bools_tuple = (True,False,True)
mix_tuple = ("red","g",3,True)

names = ("kim","ah","ran")
first_name = names[0]
second_name = names[1]
third_name = names[2]
print(first_name)
print(second_name)
print(third_name)
print(names[-1])

list = [1,2,3]
tuple = (1,2,3)
print(list)
print(tuple)

list[0] = 30
print(list)

#tuple[0] = 30
#print(tuple)

list.append(4)
print(list)
#tuple.append(4)
#print(tuple)
#파이썬이 변수를 까먹을 수 도 있어서 튜플을 사용할 경우 변하지 않고 안정적으로 보관 가능

multi_tuple = (1,(2,3),[4,5])
print(multi_tuple[2])
print(multi_tuple[1][1])

multi_tuple[2][0] = 3 # 리스트는 튜플 안에 있더라도 수정 가능함
print(multi_tuple[2])

slice_tuple = (3,20,"파이썬",True,"고양이",23)
print(slice_tuple[0:8])#범위를 벗어나도 출력가능
print(slice_tuple[8:50])#범위를 완전히 벗어나면 빈칸
#print(slice_tuple[10])오류남. 인덱스 안됨

#튜플메서드
#count: 튜플에서 특정 값이 몇번 등장하는지
#index: 특정 값이 처음 등장하는 위치(인덱스)를 찾아줌

count_tuple = (1,2,3,2,2,4,5)
count_of_2 = count_tuple.count(2)
print(count_of_2)

index_tuple = (10,20,30,40,50)
index_of_20 = index_tuple.index(20)
print(index_of_20)
print(len(index_tuple))#길이를 반환해 주는 것
print(40 in index_tuple)#40이 index_tuple에 있니

tuple1 = (1,2)
tuple2 = (3,4)
print(tuple1 + tuple2)#수정이 안되는 대신 합칠 수 있음

print(tuple1*3)#튜플 3번 반복

a = 10 #변수
b = 20 #변수
print(f"교환 전 : a:{a}, b:{b}")
a,b = b,a # 변수 값을 기반으로 튜플 생성.두개
#괄호가 없어도, ","가 있다면 튜플로 간주함❗❗❗❗❗❗❗❗❗❗❗
print(f"교환 후 : a:{a}, b:{b}")
# 튜플은 변하지 않지만 서로 가지고 있는 값을 교환할 수 있다.