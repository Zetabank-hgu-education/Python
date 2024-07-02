# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/10 2000년
# [코드]
# Class House:
# 	# 매물 초기화
# 	def __init__(self, location, house_type, deal_type, price, completion_year):
# 		pass

# 	#매물 정보 표시
# 	def show_detail(self):
# 		pass

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self): # 해당매물의 정보 출력하는 메서드
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year)
        
        
houses = [] # HOUSE 객체를 담는 리스트 생성
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/5", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses))) # 전체 매물 개수 출력
for house in houses:
    house.show_detail() # HOUSE 객체에 대한 쇼 메서드 호출 ( 매물 세부 정보 출력 )
