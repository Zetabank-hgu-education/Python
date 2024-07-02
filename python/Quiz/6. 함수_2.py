def solution(start_num, end_num):
    # 시작 숫자부터 종료 숫자까지의 리스트 생성
    num_list = list(range(start_num, end_num + 1))
    return num_list

# 예시 테스트
print(solution(1, 5))   # 출력: [1, 2, 3, 4, 5]
print(solution(0, 3))   # 출력: [0, 1, 2, 3]
print(solution(10, 15)) # 출력: [10, 11, 12, 13, 14, 15]
print(solution(-5, 0))  # 출력: [-5, -4, -3, -2, -1, 0]

