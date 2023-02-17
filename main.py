# import operator
#
# i = 5
# j = 2
#
# print(operator.floordiv(i, j))
# print(operator.pow(i ,j))


#take input in celcius and convert into farenheight
# import operator
# c = int(input("Enter value"))
# f= operator.add(operator.mul(c,1.8),32)
# print(f)


# i = int(input("Enter num"))
# # num = i.split()
# str=str(i)
# for x in i:
#     if int(x[0]) + int(x[1]) == int(x[2]):
#         print(True)

# i = int(input("Enter num"))
# sum= int(i[0]) + int(i[1])
# print(sum)



# num = input("enter a 3 digit number:")
# sum = int(num[0]) + int(num[1])
# if sum == int(num[2]):
#  print(f"{num} is a handsome number")
# else:
#     print(f"{num} is not a handsome number")




# import math
# i = int(input("Enter num"))
# if (i>99 and i<999):
#     l_index = i % 10
#     i = math.floor(i/10)
#
#     m_index = i % 10
#     i = math.floor(i / 10)
#
#     f_index = i % 10
#
#     if ((f_index + m_index) == l_index):
#         print("hansome number")
#     else:
#         print("not hansome number")



# import operator
#
# a = int(input("please enter three digits number: "))
#
# res = [int(x) for x in str(a)]
#
# print(operator.add(res[0],res[-1]))




# def fun(a, *args):
#     for arg in args:
#         print(arg)
#
# def fun(a, *args):
#     print("HEllo")
#
# fun(123,1233,1212,12,1)


# a = "abcbed"
# sum = 0
# for i in a :
#     sum +=ord(i)
# print(sum)


# i = 'AkashLokhande'
# sum=0
# for x in i:
#     sum +=ord(x)
# print(sum)

# n= int(input("Enter value: "))
# sum = 0
# for x in range(1, n):
#     if(n % x == 0):
#         sum = sum + x
# if (sum == n):
#     print("Number is The Perfect number")
# else:
#     print("Number is not perfect number")

# import math
# def quad(*args):
#     print("Permeter: ",sum(args))
#     print("Area: ",math.prod(args))
#     d =
#
# a=10
# b=20
# c=30
# d=40
# quad(a,b,c,d)



# import math
# def calc(*args):
#  print("Perimeter ", sum(args))
#  print("Area", math.prod(args))
# p = math.sqrt(((args[0] * args[2])+(args[1] * args[3]))*((args[0] * args[3])+(args[1] * args[2]))/ ((args[0] * args[1])+(args[2] * args[3])))
# q = math.sqrt(((args[0] * args[2])+(args[1] * args[3]))*((args[0] * args[1])+(args[2] * args[3]))/ ((args[0] * args[3])+(args[1] * args[2])))
# return [p, q]
# diagonals = calc(1,2,3,4)
# print(f"daigonal is {round(diagonals[0], 2)}, {round(diagonals[1], 2)}")



# def hello(u):
#     for i in u:
#         yield i * i
# print(list(hello([1,2,3,4,5,6])))


# i= [12344556545]
# d={}
# for x in i:
#     d[items]= i.count(items)
#
# for key , value in d.items():
#     print("%d : %d"%(key , value))
# print(d)


# i = int(input("Please enter numbers : "))
# l = []
# for j in str(i):
# l.append(j)
# l2= set(l)
# print(l)
# print(l2)
# for s in l2:
# print(f'{s}={l.count(s)}')



from math import sqrt
def solve(n):
   sq_root = int(sqrt(n))
   return (sq_root*sq_root) == n
n = 36
print (solve(n))