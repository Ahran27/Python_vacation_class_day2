fruit_colours = {
    "red" : "apple",
    "yellow" : "banana",
    "purple" : "blueberry"
}

for i in fruit_colours:# 키값만 출력
    print(i)

sports_stars = {
    "축구": "손흥민",
    "피겨" : "김연아",
    "수영" : "박태환",
    "펜싱" : "박상영"
}

for i, star in sports_stars.items():# 키값 전부 뽑기
    print(i)
    print(star)

sports_list = list(sports_stars.keys())
print(sports_list)

sports_list.append("농구")
print(sports_list)

for i in sports_list:
    print(i)

sports_stars["농구"] = "서장훈"
print(sports_list)
print(sports_stars.items())
