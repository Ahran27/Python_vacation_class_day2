'''
open("파일이름","모드")

✔모드
1. "r": 읽기 모드
2. "w": 쓰기 모드
3. "a": 추가 모드

✔파일 읽기
1. 변수명.read(): 파일 전체 내용 읽기
2. 변수명.readline(): 파일 한 줄씩 읽기
3. 변수명.readlines(): 파일의 모든 줄을 읽어 리스트로 반환
'''

file = open("text.txt","r")#텍스트 파일을 가져올 때 아스키코드로 갖고오기때메 영어텍스트로 실습
file_read = file.read()
print(file_read)

file2 = open("text.txt","w")#다른 파일의 데이터를 수정
file2.write("I want to go to my home.")

file2.close()#메모리 감소위함. 가방을 닫는다고 생각하면 됨

