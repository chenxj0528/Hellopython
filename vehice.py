try:
    int('123')
except ValueError as reson:
    print(reson)
else:
    print("最后被打印")
finally:
    print("最后被打印2")
