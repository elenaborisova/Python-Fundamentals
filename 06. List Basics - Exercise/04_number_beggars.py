numbers = list(map(int, input().split(", ")))
beggars_count = int(input())

money_sum = []
index = 0
count = 0

for num in numbers:
    if index >= len(money_sum):
        money_sum.append(0)

    money_sum[index] += num
    index += 1
    count += 1
    if count == beggars_count:
        index = 0
        count = 0

if len(money_sum) < beggars_count:
    difference = beggars_count - len(money_sum)
    for i in range(difference):
        money_sum.append(0)

print(money_sum)
