import time

from day2.숫자형 import second


def timer(second,callback):#특정시간 이후에 나오게
    #second: 몇초 동안 기다릴건지
    #callback: 시간을 기다린 후에 실행할 함수를 콜백으로 받음
    print("타이머시작")
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    #time.sleep(5)5초동안 멈춤
    callback()
    #second에 입력한 초를 기다린 후 콜백으로 전달받은 함수를 실행
    print("타이머 종료")

def callback():#timer안에서 작동할 함수
    print(f"{second}초 뒤 실행된 함수입니다.")

timer(3,callback)
