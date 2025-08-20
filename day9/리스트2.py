'''
append(): 리스트 마지막에 새로운 요소 추가
insert(): 중간에 추가

sort(): 오름차순(원본이 변경됨)
sort(reverse = True): 내림차순

remove(): 리스트 삭제
pop(인덱스 번호): 특정위치 삭제

join(): 리스트에 새로운 것을 추가해 하나의 문자열로 결합

reverse: 역순
#x in y: x가 y 안에 있으면 True / False

text = "hello world"
print("hello" in text)
print("java" in text)
'''

append_nums = [1,2,3]
print(f"append_nums() 추가 전 : {append_nums}")
append_nums.append(4)
print(f"append() 추가 후 : {append_nums}")

append_nums.insert(0,0)
print(f"insert()추가 후: {append_nums}")

remove_nums = [1,2,3]
remove_nums.remove(3)#마지막자리가 2니깐
print(remove_nums)

remove_nums.pop(1)#인덱스 번호
print(remove_nums)

reversed_nums = [2,4,6,8,10]
reversed_nums.reverse()
print(reversed_nums)

join_text = ['a','b','c']
join_result = "-".join(join_text)
print(join_result)

sort_text = ['나','다','가','사','라']
sort_text.sort()
print(sort_text)

numbers = [3,7,8,6,10,4,2,5,0,1]

print(3 in numbers)

new_list = []
for num in numbers:
    if num > 5:
        new_list.append(num)# 누 리스트에 새로운 요소 추가
new_list.sort()
print(new_list)

#x in y: x가 y 안에 있으면 True / False

text = "hello world"
print("hello" in text)
print("java" in text)

#바 가 들어있는 단어들만 새 리스트에 추가
words = ["사과", "바나나", "포도", "딸기", "망고", "바람", "바이올린"]
bar_words = []
#if에도 in 사용가능
for word in words:
    if "바" in word:
        bar_words.append(word)
print(bar_words)