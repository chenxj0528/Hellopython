# a = [i for i in range(100) if not i % 2 and i % 3]
#
# print(a)


# b = {i: i % 2 == 0 for i in range(10)}
# print(b)

# c = {i for i in [1, 1, 2, 2, 5, 5, 6, 6, 8, 8]}
# print(c)

# d = "i for i in 'ABCDEFGHIJKLMN'"
# print(d)

e = (i for i in range(100) if i % 2)

for i in e:
    if i > 60:
        break
    print(i)

print(sum(e))
