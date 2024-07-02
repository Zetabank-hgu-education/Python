# #1-1 module
# import theater_module
# theater_module.price(3) #3명에서 영화보러 갔을 때 가격
# theater_module.price_morning(4) #4명에서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) #5명의 국인이 영화 보러 갔을 때

# import theater_module as mv #theater_module을 mv로 간추려서 호출 가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * #theater_module 없이 이 모듈을 모두 사용하겠다
# price(3)
# price_morning(4)
# price_soldier(5)

#1-2 package

# import travel.thailand # 맨뒤에 thailand부분에는 모듈이나 패키지만 가능 
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from을 이용하면 class나 함수를 바로 이용 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#1-3
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# #1-4
# import inspect
# import random
# print(inspect.getfile(random))

# # 1-5
# from travel import * 
# import inspect
# print(inspect.getfile(thailand))
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 1-6
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# # 1-7 외장함수 time
# import time

# def timer(seconds):
#     print(f"타이머 시작: {seconds}초")
#     while seconds:
#         mins, secs = divmod(seconds, 60)
#         time_format = '{:02d}:{:02d}'.format(mins, secs)
#         print(time_format, end='\r')
#         time.sleep(1)
#         seconds -= 1
#     print("타이머 종료!")

# # 10초 타이머 실행
# timer(10)

# # 1-8 외장함수 random

# import random

# # 주사위 굴리기 함수
# def roll_dice():
#     dice = random.randint(1, 6)
#     print(f"주사위 결과: {dice}")

# # 주사위 5번 굴리기
# for _ in range(5):
#     roll_dice()

# #/ 실제로는 개발자가 공개범위를 설정해줘야함 / 공개하고싶은것은 import 가능