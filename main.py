from re import split

# s = input()
# slower = s.lower()
# # s1 = s[::-1]
# lst = slower.split(maxsplit=-1)
# s2 = ''.join(lst)
# s3 = s2[::-1]
# if s3 == s2:
#      print("True")
# else:
#      print("False")

# lst = ["Я", "пишу", "программы", "на", "Питоне"]
# print(' '.join(lst))
# print

# str.split(sep=None, maxsplit=-1)
# print("Don't worry be happy".split(maxsplit=-1))
# ab = "abcdefghijklmnopqrstuvwxyz"
# res = []
# for i in range(len(ab)):
#      x = ab[i]
#      a = x*(i+1)
#      res.append(a)
# print(res)

# su = 0
# while True:
#      n = int(input())
#      if n < 0:
#           break
#      su += n
# print(su)

# tpl = (123, 234, 345, 456)
#
# n = tuple(input())
# tpl2 = tpl + n
# tpl2 = sorted()
# print(tpl2)

su = 0
len1 = 0
while True:
     n = int(input())
     len1 += 1
     if n == 0:
          break
     su += n
su1 = su / len1
print(su1)
print(len1)