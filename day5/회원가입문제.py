# 아이디와 숫자비밀번호를 입력받음
# 아이디와 비밀번호가 모두 일치한다면 로그인 되었습니다
# 아이디가 맞지 않다면 아이디를 다시 입력해주세여
# 비밀번호가 틀렸다면 비밀번호 불일치
# 아이디 비밀번호 불일치 회원가입 하러가기
# 내 답
"""
login_id = input("아이디를 입력하세요: ")
login_pw = int(input("비밀번호를 숫자로 입력하세요: "))


if login_id == "correctid" and login_pw == 1234:
    print("로그인 되었습니다.")
elif login_id != "correctid":
    print("아이디를 다시 입력해주세요.")
elif login_pw != 1234:
    print("비밀번호가 불일치합니다.")
else:
    print("회원가입 하러 가기->")
"""

#선생님 답
id = input("아이디를 입력하세요: ")
pw = int(input("비밀번호를 숫자로 입력하세요: "))

correct_id = "ahran"
correct_pw = 1234

if id == correct_id and pw == correct_pw:
    print("로그인 되었습니다.")
elif id != correct_id and pw == correct_pw:
    print("아이디를 다시 입력해주세요.")
elif id == correct_id and pw != correct_pw:
    print("비번 불일치")
else:
    print("아디 비번 불일치 회원가입하러가기")