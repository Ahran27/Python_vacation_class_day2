'''
2중 for문과 range를 사용하여
1
22
333
4444
55555
출력하기
for number in range(1,5):
    for num_re :
        print(number,num)
'''
n = 5
for i in range(1,n+1): # 6이 되어야 5까지 출력하기 때문
    for j in range(i):# 한번 돌 때 j는 i 만큼 출력
        print(i, end =" ")
    print()#줄바꿈. 숫자 바뀔 때 줄이 바뀜