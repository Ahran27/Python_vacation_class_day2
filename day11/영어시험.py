'''

'''
def english_quiz(questions,answers,name):
    score = 0
    student_answers = []

    for i in range(len(questions)): #문제 갯수를 돌아야 함
        ans = input(f"'{questions[i]}'의 영어 단어를 입력하세요: ")
        student_answers.append(ans)#빈 리스트에 받아 온 답 추가

        if ans.lower() == answers[i].lower():
            score += 10
    print(f"{name}의 점수는 {score}입니다.")
    print("입력한 답 : ",student_answers)

questions = ["사과","바나나","체리"] # 출제용 한글 단어 리스트
answers = ["apple","banana","cherry"] # 정답 리스트

name = input("학생 이름 입력: ")

english_quiz(questions,answers,name)