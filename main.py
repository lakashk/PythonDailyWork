# a ,b ,c = input("Enter 3 string\n").split(" ")
# print(a,b,c)


# i= 123
# s =str(i)
# print(s)
# print(s[int(len(s))-1])

# sample = "Hello there"
#
# #print(sample.title())
#
# print(sample + sample)
# #print(sample - sample)
# print(sample * 3)
# # print(sample - 3) #error


# i = int(input("Enter value"))
# i = str(i)
# last_d = i[len(i)-1]
# first_d = i[0]
# add = int(last_d) + int(first_d)
# print(add)

# #reversre string
# s= "This is string"
# print(s[::-1])
# print(s.split(" ")[::-1])


# i = "ABCDEF"
# # print(i[5:3])
# print(i[5:1:-1])
# print(i[5:1:-1])
# print(i[-2:-4:-1])
# # print(i[len(i)])
# print(i[-6])
#
#
# i = [0,1,2,3,4,5,6,7]
# print(i[0:6])
# print(i[4:6:2])
# print(i[0:6:4])
# print(i[0:6:2])
#
# h = "HarryPotter"
# p = "PeterPan"
# d = h[0:5]
# f = p[5::]
# print(d+f)
# # print(p[])


# str = input("Enter Input")
# print((str[::2]).upper())

temp = ''
# for i in range(len(str)):
#     if i % 2 == 0:
#         temp = temp + str[i].upper()
#     else:
#         temp = temp + str[i].lower()
# print(temp)

# for i , x in enumerate(str):
#     print(i , x)
#     if i % 2 == 0:
#         temp =temp + x.upper()
#     else:
#         temp = temp + x.lower()
# print(temp)


# count number of the vovels

# str = input("Enter Input")
# # count =0
# # for i in str:
# #     if i in ('a','e','i','o','u'):
# #         count = count + 1
# # print(count)
#
# k = str.lower()
# total = 0
# total += k.count('a')
# total += k.count('e')
# total += k.count('i')
# total += k.count('o')
# total += k.count('u')
# print(total)



#Triangular number
# i = int(input("Enter number"))
# sum=0
# for x in range(1, i):
#     sum = sum + x
#     if sum == i:
#         print("Triangular")
#         break
#     else:
#         print("Not Triangular")

# sum_array = []
# sum_n = 0
# n = int(input("Enter a number:"))
# for i in range(n):
#     sum_n = sum_n + i
#     sum_array.append(sum_n)
# if n in sum_array:
#     print("It is a triangular number")
# else:
#     print("It's not a triangular number")


# def temp_function():
#     for i in range(0 , 100 , 5):
#         yield i
# temp = temp_function()
# print(temp.__next__())
# print(temp.__next__())
# print(temp.__next__())

# def temp_function(range):
#     for i in range(0 ,5):
#         print((i+1) * "0")


#Palindrome
# i = [1,2,3,4]
# #stack -- lifo
#
# i.pop(-1)
# print(i)

# str = input("enter string")
# temp_list = []
# for i in str:
#     temp_list.append(i)
# reversed_list = temp_list[::-1]
# print(reversed_list, temp_list)
# if reversed_list == temp_list:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# dict = {"name": "Lokhande", "num": 1, "DOB":1998}
# print(dict["num"])
#
#
# dict1 = {"name": "Akash", "usn": "101", "Location":"Pune"}
# n = input("Enter text")
# list = [dict, dict1]
# for item in list:
#     if n in item["name"]:
#         print(True)
#         print(dict1)
#     elif n in item["name"]:
#         print(dict)

dict = {"name": "Lokhande", "num": 1, "DOB": 1998}
dict1 = {"name": "Akash", "usn": "101", "Location":"Pune"}
dict2 = {"name": "nsdjkd", "usn": "101", "Location":"Pune"}

temp = [dict,dict2,dict1]

sh= input("enter value")
sh=sh.lower()

for i in temp:
    if i["name"].count(sh) >=1:
        print(i)
        break

    if i["usn"].count(sh) >=1:
        print(i)
        break

