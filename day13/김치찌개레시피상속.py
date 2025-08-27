class Mom:
    def make_kimchi_stew(self):
        print("엄마 레시피 : 김치 + 돼지고기 + 파 넣고 끓이기")

class Me(Mom):
    def make_kimchi_stew(self):
        #자식클래스에서 엄마와 똑같은 이름의 메서드를 새로 정의하면 자동으로 오버라이딩이 됨
        #print("내 레시피 : 김치 + 스팸 + 토마토 + 민초 넣고 끓이기")
        #ㄴ오버라이딩은 아예 덮어쓰기, super는 '거기에 내 것 추가' 너낌

        super().make_kimchi_stew()
        print("엄마의 레시피에는 민초 넣어야지~")

mom = Mom()
me = Me()

mom.make_kimchi_stew()
me.make_kimchi_stew()