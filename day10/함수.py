'''
프로그래밍 할 때 필수 기능. 특정 기능을 수행하는 집합
1. 반복적 코드 제거 및 재사용성 향상
2. 어떤 기능을 수행하는 코드인지 한 눈에 파악 가능.(가독성이 좋아짐 --> 유지보수 쉬워짐)
3. 오류 추적(디버깅) 효율적

def 함수이름():
    코드
'''

def hello():
    print("안녕하세요")
    print("저는 안나입니다.")
    print("엘사 동생이에여.")

hello()
'''
다른 언어는 들여쓰기 중요치 않음. e.g.
int hello(){
print("안녕하쇼");print("나 안나.");
    return 0;
}
'''
animals = ["강아지","고양이","햄스터","곰","기린"]
index = 0

def change_animal():
    global index # 함수 밖에서 가져올 때 global
    if index >= len(animals): #인덱스는 0이니까 변경이 안됨
        index = 0
    print(f"동물을 {animals[index]}로 변경합니다.")
    index += 1 #첫 출력 후 인덱스가 증가하며 동물이 바뀜

change_animal()
change_animal()
change_animal()
change_animal()
change_animal()
change_animal()