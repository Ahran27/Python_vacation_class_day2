#교과서에 없음
list_in_list = [1,[2,3],"hello",[True,False]]
print(list_in_list)
print(list_in_list[1][1]) #1번자리안에 1번

pythin_class = [# 대괄호사이에 콤마 필수
    ["철수","영희","민수"], #1조
    ["지수","현우","나영"], #2조
    ["동연","수진","호영"]  #3조
]

#중첩 for문으로 출력
for pyclass1_for1 in pythin_class:#1조 2조 3조 가져옴
    for pyclass_for2 in pyclass1_for1:#그 안에거 가져옴
        print(pyclass_for2)

#1조 출력
print(pythin_class[0])
#2조 출력
print(pythin_class[1])
#3조 출력
print(pythin_class[2])
#3조에 수진이 출력
print(pythin_class[2][1])
#민수 출력
print(pythin_class[0][2])
#지수가 로제로 이름을 개명한 후 2조 출력
pythin_class[1][0] = "로제"
print(pythin_class[1])

#colors라는 리스트에는 red orange green yello
#for문을 사용하여 colors라는 리스트를 돌기
colors = ["red","orange","green","yello"]
for list_colors in colors:
    print(list_colors,end=" ")