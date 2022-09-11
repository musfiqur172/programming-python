def multiplication_table(num=1):
    m = 1
    for i in range(10):
        print(num, "x", m, "=", num * m)
        m += 1


multiplication_table(8)
