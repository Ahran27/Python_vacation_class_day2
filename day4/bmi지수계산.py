#사용자의 몸무게 (소수점) 입력 받기
#키 입력받기 (170cm -> 1.7m)
#bmi = 몸무게 / 키 * 키
#당신의 bmi는 **입니다.
#weight_input = float(input("당신의 몸무게를 입력하시오 : "))
#height_input = float(input("당신의 키를 입력하시오 : [170 -> 1.7]"))
#bmi = weight_input / height_input * height_input
#print("당신의 bmi는",bmi,"입니다.")

#선생님 답
weight = float(input("몸무게를 입력하세요 : ")) #소수점 입력하기 위해 float으로 감싸기 50 -> 50.0
height_cm = float(input("키를 입력하세요 : ")) #정수를 소수점으로 단위 바꾸기
height_m = height_cm / 100 #cm ->m
bmi = weight / (height_m ** 2)
print("당신의 BMI는",round(bmi,1),"입니다") #소수점 없애는 것
