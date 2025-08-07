#문자열 길이
python_text = "python"
python_length = len(python_text)
print(python_length)

#upper() : 문자열을 대문자로 변환
#lower() : 소문자로 변환
pizza = "i love pizza"
upper_pizza = pizza.upper()
print(upper_pizza)

lower_pizza = upper_pizza.lower()
print(lower_pizza)

#strip() : 앞 뒤 공백 제거, 특정 문자 제거
cola = "         This is a cola"
strip_cola = cola.strip()
print(strip_cola)
print(cola)
#파이썬 한정. 다른 언어는 공백이 많아도 하나로 간주

coca = '--------this is-a-coca'
strip_coca = coca.strip('-')
print(strip_coca)
#스트립은 앞뒤만 제거해주고, 중간은 제거해주지 않음.
