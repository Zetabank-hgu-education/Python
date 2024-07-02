def solution(num, n):
    # num이 n의 배수인지 확인
    if num % n == 0:
        return 1
    else:
        return 0
    
print(solution(10, 2))      
print(solution(10, 3))  # 출력: 0
print(solution(15, 5))  # 출력: 1
print(solution(17, 4))  # 출력: 0

