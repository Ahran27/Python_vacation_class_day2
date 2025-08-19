students = [
    ["kim","95","  pizza  "],
    ["lee","80","pasta"],
    ["park","?","  piano"],
    ["choi","77","pancake"]
]

#for문을 사용하여 리스트에 접근할 것
print("1)변수를 만들어서 이름 첫 글자만 대문자로 보여주기")
for students_for in students: # students_for는 돌고 있는 students의 변수
    name = students_for[0].capitalize() # name은 돌고있는 Students의 변수(각 대괄호)의 0번째를 대문자화
    print(name)

        # print(students_for2.capitalize())
print("2)점수가 숫자인 학생들의 평균(정수) 구하기 (숫자가 아니면 제외)")
total = 0
count = 0
for i in students:
    score = i[1]
    if score.isdigit():
        total += int(score)
        count += 1
avg = total // count if count > 0 else 0 # count에 인원수가 안들어오면 0으로 출력
print("유효인원: ",count, "평균: ",avg)