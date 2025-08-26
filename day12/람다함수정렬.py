tuple_num = [(1,10),(4,2),(99,6),(5,1),(8,12)]
sorted_tuple1 = sorted(tuple_num)
print(sorted_tuple1)

sorted_tuple = sorted(tuple_num,key=lambda t:t[1])#t의 리턴값 정렬기준은key에서 받음
#sorted(iterable, key=함수): 이터러블인 tuple_num에서 원소를 하나식꺼내서 key에 저장된 함수에 보냄
#sorted가 정렬을 하고 싶은데 이터러블에 들어간 값을 각각 람다에게 전달해줌
#원소(1,10), (4,2) 등등등
#lambda index(1,10):index[1]

print(sorted_tuple)