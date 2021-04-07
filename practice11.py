# import theather_module

# theather_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theather_module.price_morning(4)
# theather_module.price_soldier(5)

# from theather_module import price_soldier as price
# # price(5)
# import travel.thailand
# # import travel.thailand.ThailandPackage 이런식으로는 사용 불가 import에는 모듈이나 패키지만 (함수나 클래스가 올 수 없음)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# import inspect
# import random
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# # print("{0}은 아주 좋은 언어입니다.".format(language))
# import random  # 외장 함수
# print(dir())
# # dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# name = "Jim"

# print(dir(name))
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 ", today + td)
