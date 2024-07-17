def sum_avg(*li):
    sum = 0
    for i in li:
        sum += i
    return sum, sum/len(li)

print(sum_avg(1, 2, 3, 4, 5))
print(sum_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))