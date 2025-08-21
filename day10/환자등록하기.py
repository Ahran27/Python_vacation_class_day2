'''
환자를 담을 빈 리스트 생성

몇명의 환자를 등록할 것인지 물어보기

*번째 환자 이름 : 입력받기
*번째 환자 체온 입력받기

비어있는 환자 리스트에 이름과 체온 튜플로 추가하기
'''
"""hospital = []
patients = int(input("몇 명의 환자를 등록하시겠습니까? : "))
count = 1
if patients != 0:
    name = input(f"{count}번째 환자 이름 : ")
    degree = input(f"{count}번째 환자 체온 : ")
hospital.append(name,degree)
"""

patients = []
q = int(input("몇 명의 환자를 등록하시겠습니까? : "))

for i in range(q):#몇명 입력했는지 모르니까 for문으로 정해줌
    name = input(f"{i+1}번째 환자 이름 : ")
    temp = float(input(f"{i+1}번째 환자 체온 : "))
    patients.append((name,temp))#튜플로 추가할거니까 괄호 한번더

def check_patients(patients_list,fever=37.5):
    print("환자 발열 검사 결과")
    for user, fever_check in patients_list:
        if fever_check >= fever:
            print(f"{user} : {fever_check} 발열환자입니다.")
        elif fever_check <= 36.0:
            print(f"{user} : {fever_check} 저체온증 환자입니다.")
        else:
            print(f"{user} : {fever_check} 정상입니다.")

check_patients(patients)