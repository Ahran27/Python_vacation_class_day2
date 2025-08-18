'''
사용자에게 영화 이름을 입력받은 후
계속 반복하는 while문 시작
영화 평점 입력받기 (1~5) 사이로
1~5평점이 입력되었다면
    기생충의 평점 : *****
1부터 5 사이의 숫자를 입력하세요 출력 후 다시 별점 입력받으러 가기
'''
film = input("영화의 제목을 입력하세요.: ")

while True:
    score = int(input(f"{film}의 평점을 입력하시오(1~5): "))
    if 1 <= score <= 5:
        print(f"{film}의 평점 : " + "★" * score)
    else:
        print("🤔잘못입력하였습니다. 다시 입력하세요")
        continue
    break