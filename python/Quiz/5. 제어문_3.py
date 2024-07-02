# 쇼핑 목록을 관리하는 밑의 기능이 포함된 프로그램을 작성해보세요.

# 항목 추가 : 사용자가 “완료＂를 입력할 때까지 쇼핑 목록에 항목 추가 가능
# 목록 출력 : 최종 쇼핑 목록을 출력

# [예시]
# Shopping_list = []
# While문, input함수를 활용하여 shopping_list안에 항목 추가, 완료를 입력하면 종료
# For문을 통해 shopping_list안에 있는 품목 출력


shopping_list = []

while True: # 특정 조건이 True가 될때까지 무한 루프
    item = input("쇼핑 목록에 추가할 항목을 입력하세요 (완료를 입력하면 종료): ")
    if item == "완료":
        break
    shopping_list.append(item)

print("\n최종 쇼핑 목록:")

for item in shopping_list:
    print("- " + item)