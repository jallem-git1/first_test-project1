# stars = ['11','22','33','44','55','66','77']

# eachstar = iter(stars)
# print(type(eachstar))

# each = enumerate(stars)
# print(type(each))

# for no in each:
#     print(no)

nums = [(1,2),(3,4),(5,6)]

data = [1, 2, 'a', 'b', 4, 5]
def mysum(a):
    return a[0]+a[1]

result = filter(lambda x: isinstance(x, int), data)
print(list(result))

# rr = map(mysum, nums)
# print(list(rr))

kk=isinstance(11, int)
print(kk)