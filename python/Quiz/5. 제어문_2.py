# Input함수와 if문을 이용하여 적절한 복장을 추천하는 프로그램 제작

# 온도 30 이상 : 반팔과 반바지
# 온도 20 이상 30 미만 : 반팔과 긴바지
# 온도 10 이상 20 미만 : 긴팔과 바람막이
# 온도 0 이상 10 미만 : 코트와 스웨터
# 그 외 온도 : 패딩과 모자


temperature = int(input("현재 온도를 입력하세요 : "))
if temperature >= 30:
    outfit = "반팔과 반바지"
elif 20 <= temperature < 30:
    outfit = "반팔과 긴바지"
elif 10 <= temperature < 20:
    outfit = "긴팔과 바람막이"
elif 0 <= temperature < 10:
    outfit = "코트와 스웨터"
else:
    outfit = "패딩과 모자"
    

print(f"현재 온도는 {temperature}도 입니다. 추천 복장: {outfit}")