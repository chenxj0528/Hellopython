# dict1 = {'a':'A','b':'B','c':'C','d':'D'}

# for i in dict1:
#     #print('%s --> %s' % (i, dict1[i]))
#     print(f'{i} --> {dict1[i]}')

# it = iter(dict1)
#
# while 1:
#     try:
#         print(dict1[next(it)])
#     except:
#         break

class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


f = Fibs(2)

print(f)
print(type(f))
a = iter(f)
print(a)
print(type(a))

print(isinstance(a, Fibs))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
