#사용자에게 나이를 입력받음
#사용자에게 키를 입력받음
#정수로 입력받음
#키가 120이상, 나이가 10살 이상이어야만 탑승 가능
#탑승 여부는 true / false로 구분
'''
age = int(input("탑승자의 나이를 입력하시오: "))
height = int(input("탑승자의 키를 입력하시오: "))
result = age >= 10 and height >= 120
print(result)
'''
#선생님 답
height = int(input("탑승자의 키를 입력하시오: ")) #flaot나 int가 꼭 들어가야 하는 이유는, input으로 받은 답은 문자로 인식하기에
age = int(input("탑승자의 나이를 입력하시오: "))
can_ride = height >= 120 and age >= 10
print("놀이기구를 탈 수 있나요?",can_ride)
