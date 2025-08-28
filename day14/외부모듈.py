'''
터미널 : pip install 모듈이름
pip install Flask(윕서버를 구축하는 것) / Django
pip install beautifulsoup4 / request- 웹에서 데이터 불러와서 분석하기
pip install tensorflow (간단한 인공지능 갖다가 쓰기~)/ scikit-run
cv2 / pillow 영상 위한 모듈
python midi 음악 위한 모듈

1. 데이터 수집 목적은 반드시 학습, 연구로 써야함(상업적, 불법 X)
2. 악용 X
3.
'''
from bs4 import BeautifulSoup
from urllib import request

weather_url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250828.xml"
data = request.urlopen(weather_url)

with request.urlopen(weather_url) as response:
    soup = BeautifulSoup(response,"xml")

for location in soup.select("local_ta"):
    city = location.select_one("local_ta_name").get_text(strip = True)
    print(f"\n{city}")# \n -> 줄바꿈

    for i in range(1,5):
        base = f"week{i}_local_ta_"
        normal = location.select_one(base + "normalYear").get_text(strip = True)
        rng = location.select_one(base + "similarRange").get_text(strip = True)
        minv = location.select_one(base + "minVal").get_text(strip = True)
        maxv = location.select_one(base + "maxVal").get_text(strip = True)
        sim = location.select_one(base + "similarVal").get_text(strip = True)
        print(f"{i}주차 | 평균 {normal}도 | 범위{rng}도 | 최저 {minv}도 | 최고 {maxv}도 | 유사사례 {sim}")