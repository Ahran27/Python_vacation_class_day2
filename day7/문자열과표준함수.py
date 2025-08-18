print("babo")
print("1234")

text = "안녕하쇼마이~"
print(text[-1]) # 뒤에서부터

# text[-1] = "!" ---> 이 자리에 !를 대입하겠다. 근데 오류남. 문자열은 바꿀 수 없음


"""
❕❕❕대소문자 변환
upper(): 대문자로 변환
lower(): 소문자로 변환
capitalize(): 첫 글자만 대문자로 변환

❕❕❕문자열 찾기
fine(): 특정 글자가 어디있는지 찾기
count(): 특정 글자가 몇 번 등장하는지 세기

❕❕❕문자열 변경하기
replace(): 특정 글자를 다른 글자로 바꾸기

❕❕❕문자열 나누고 합치기
split(): 특정 기준으로 문자열 나누기(리스트로 변환)
join(): 리스트를 문자열로 합치기

❕❕❕공백제거하기
strip(): 양 쪽 공백 제거
lstrip(): 왼쪽 공백 제거
rstrop(): 오른쪽 공백 제거

❕❕❕문자열이 특정 조건을 만족하는지 확인
startswith(): 특정 문자로 시작하는가
endswith(): 특정 문자로 끝나는가
isdigit(): 숫자로만 이루어져있는가
isalpha(): 알파벳으로만 이루어져있는가
"""

money = "money"
print(money.capitalize())

find_text = "find text"
print(find_text.find("text"))  # 5번째에서 시작하고 있다.
print(find_text.find("java"))  # 찾는 값이 없으면 -1을 출력함

banana = "banana"
print(banana.count("a"))  # a의 갯수를 찾아줘

replace_text = "I like dog"
print(replace_text.replace("like","love"))  # 안에는 바꿀 값을 넣고 뒤에는 바꿀 내용