#while 안에 반복문이 더 있는 것 e.g. 4일간 2시간 반복한다
#5개행 2열
row = 1
while row <= 5:
    column = 2
    while column <=2:
        print("{}행 {}열".format(row,column)) #f는 format. 옆의 괄호 수 만큼 값을 넣어줘야 함. e.g. f"{},{}"이라고 쓰거나 "{},{}"format()쓰고 괄호수만큼 인자 넣어도 됨
        column += 1
    row += 1
    print(" ")

