temperature = list(map(int, input().split()))

sum_num = sum(range(temperature[0],temperature[-1] + 1)) 
print(sum_num)
LEN = len(temperature)
print(LEN)
AVG = sum_num / LEN
print(AVG)


