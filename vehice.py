def jiecheng(x):
    if x == 1 or x == 2:
        return 1
    else:
        return jiecheng(x - 1) + jiecheng(x - 2)


a = jiecheng(40)

print(a)
