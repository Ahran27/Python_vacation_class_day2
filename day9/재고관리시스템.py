inventory = {
    "콘칩" : 10,
    "오징어집" : 3,
    "레이" : 7,
    "칸초" : 0

}
#재고가 0이라면 재고가 없습니다!
#5개 미만이라면 재고가 부족합니다.
# 위 조건에 걸리지 않는다면 재고 충분!
#for i, star in sports_stars.items():# 키값 전부 뽑기
    #print(i)
   # print(star)


for name, stock in inventory.items():#키와 값을 받아옴.for 키, in 값
    if  stock == 0:
        print(f"{name} 재고가 없습니다")
    elif stock < 5:
        print(f"{name} 재고가 부족합니다. 현재 {stock}개 남음")
    else:
        print(f"{name} 재고가 충분합니다. 현재 {stock}개")

