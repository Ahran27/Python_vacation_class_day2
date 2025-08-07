#4자리 학번을 입력받아
#슬라이싱을 학년, 반, 번호, 추출하기
#학년은 첫째자리
#반은 둘째자리
#번호는 3-4번
#123 --> 1학년 2반 34번

#내 답 : 이렇게 하면 나중에 문자열 번호까지 계속 같이 입력해야함
student_code = input("4자리 학번을 입력하세요 : ")
print(student_code[0],"학년",student_code[1],"반",student_code[2:4],"번")

#선생님 답 - 포맷팅하는것. 변수에 중괄호를 넣고 앞에 f만 붙이면 됨. 이렇게 하면 나중에 변수 이름만 쓰면 문자열 번호 쓸 필요 없음
student_id = input("4자리 학번을 입력하세요 : ")
grade = student_id[0]
class_num = student_id[1:2]
student_num = student_id[2:4]
print(f"{grade}학년 {class_num}반 {student_num}번")