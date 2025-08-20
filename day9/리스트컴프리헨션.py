#새리스트 = [표현식 for 반복문 이름 in 반복할 리스트]
numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)

number = [i+1 for i in range(1,11)] # for문을 돌거다. i의 값을 변형없이 표현하겠다
print(number)

even_nums = [i for i in range(1,11) if i % 2 == 0]#i가 2로 나눴을 때 0이라면 i를 출력
print(even_nums)

result = []
for i in range(1,11):
    if i % 2 == 0:
        result.append("짝수")
    else:
        result.append("홀수")
print(result)

result2 = ["짝수" if i % 2 == 0 else "홀수" for i in range(1,6)]#i가 2로 나눴을 때 0이라면 "짝수" 출력, 아니라면 "홀수"
print(result2)

list_in_list  = [
    [1,3,5],
    [6,9,12],
    [15,18,21]
]

#3의 배수
list_in_list_three = []
for row in list_in_list:#list_in_list에서 안에 있는 리스트를 뽑을거다. 각 리스트는 row라고 부른다
    for num in row:#각 row안에 있는 num을 뽑는다
        if num % 3 == 0:#만약에 num이 3의 배수라면
            list_in_list_three.append(num)#리스트2에 num을 추가(새 리스트에 3배수만 추가됨)

list_in_list_three2 = [num for row in list_in_list for num in row if num % 3 == 0]#맨 앞에 num. 마지막에 남는 것은 num일거다
print(list_in_list_three2)

print(list_in_list_three)

#[] / for문
#list_in_list[0][1]
print(list_in_list[0][1])

for row_index_one in list_in_list:
    #print(row_index_one[1])
    print(row_index_one)



