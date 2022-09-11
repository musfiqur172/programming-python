def average(li):
    sum = 0
    for num in li:
        sum += num

    result = sum / len(li)
    return result


li = [1, 2, 3, 4]
print(average(li))
