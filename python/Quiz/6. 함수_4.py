def solution(n):
    return str(n)

# 예시 테스트
print(type(solution(123)))  # 출력: "123"
print(solution(123))  # 출력: "123"
print(solution(0))    # 출력: "0"
print(solution(-456)) # 출력: "-456"


def solution(num_list):
    # 리스트를 오름차순으로 정렬합니다.
    num_list.sort()
    # 가장 작은 5개의 수를 반환합니다.
    return num_list[:5]

# 예시 테스트
print(solution([10, 3, 5, 1, 4, 2, 7, 9, 8, 6]))  # 출력: [1, 2, 3, 4, 5]
print(solution([30, 10, 20, 50, 40, 60, 70]))     # 출력: [10, 20, 30, 40, 50]
print(solution([1, 2, 3, 4, 5]))      