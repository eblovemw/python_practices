# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

nums = [6, 8, 9, 20, 21, 26, 29, 33, 37, 39, 41, 42]

count = 0
total = 0

for i in nums:
    if i % 3 == 0:
        total += i
        count += 1

print("주어진 리스트에서 3의 배수의 개수 => ", count)
print("주어진 리스트에서 3의 배수의 합 =>", total)