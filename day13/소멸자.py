"""
파이썬에는 쓰레기통(garbage collector)이 있기 때문에 알아서 필요 없는 객체를 삭제한다.
__del__:지우는 것. 계속 메모리에 남아있을 때 언젠가 메모리 누수(프로그램 터짐)가 올 수 있음
"""
#알아서 파일 만들고 안에 내용 적기
class FileHandler:
    def __init__(self,filename):
        self.file = open(filename,'w')
        print(f"{filename}파일을 열었습니다.")

    def write_data(self,data):
        self.file.write(data)

    def __del__(self):#__del__실행이 되고 삭제되기 전 마지막 출력
        self.file.close()
        print("파일을 닫았습니다")

handler =  FileHandler("del_text.txt")
handler.write_data("hello. python")
del handler