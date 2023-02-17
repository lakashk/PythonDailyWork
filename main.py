# #hackerrank Q rangoli
# cstr = "ABCD"
# print("The Centre aligned string is :")
# print(cstr.center(10,'-'))
# print(cstr.ljust(10,'-'))
# print(cstr.rjust(10,'-'))
#
#
# #Hackerrank  Q string formating
# i = 17
# s='1     1     1     1'
# for i in range(1,18):
#     print(str(i),
#           format(i , "o").rjust(2," "),
#           format(i , "x").upper().rjust(2," "),
#           format(i, "b").rjust(2," "))
import json

# f = ["apple", "banana", "cherry","mango"]
# new = [i for i in f if "a" in i]
# print(new)
#
# f = [1,2,3,4,5,6]
# n = [x for x in f if x > 3]
# n = [x for x in f if len(str(x)) == 1]
# print(n)
#


#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
#
# newlist = [i for i in fruits if "a" in i]
# print(newlist)
#
# student_1 ={
#     "name": "Cezane",
#     "USN":"006644",
#     "locaion": "Nepal"
# }
#
# student_2 ={
#     "name": "Junee",
#     "USN":"113322",
#     "locaion": "Nepal"
# }
#
# student_3 ={
#     "name": "Anish",
#     "USN": "1133222",
#     "locaion": "Nepal"
# }
#
# student_4 ={
#     "name": "Nisht",
#     "USN": "1133222",
#     "locaion": "Nepal"
# }
#
# friend_list = [student_1, student_2, student_3, student_4]
#
#
#
# student_1 ={
#     "name": "Cezane",
#     "USN":"006644",
#     "locaion": "Nepal"
# }
#
# student_2 ={
#     "name": "Junee",
#     "USN":"113322",
#     "locaion": "Nepal"
# }
#
# student_3 ={
#     "name": "Anish",
#     "USN": "1133222",
#     "locaion": "Nepal"
# }
#
# student_4 ={
#     "name": "Nisht",
#     "USN": "1133222",
#     "locaion": "India"}
# friend_list = [student_1, student_2, student_3, student_4]
#
# # my_list = [x for x in fruits if len(str(x)) == 1]
# # print(my_list)
#
# print(friend_list)
#
#
# my_nepal = [x for x in friend_list if x["locaion"]=="Nepal"]
# print(my_nepal)
#
# my_india = [x for x in friend_list if x["locaion"]=="India"]
# print(my_india)
#
# usn = [x for x in friend_list if x["USN"].count("3")>=1 ]
# print(usn)
#
# name = [x for x in friend_list if x["name"].count("ee")>=1]
# print(name)
#
#


## install request package in python
#get
#post
#delete
#update

# import requests
# request_url = "https://jsonplaceholder.typicode.com/todos/1"
#
# respose = requests.get(url = request_url)
# print(respose)
# print(respose.text)
# print(respose.json())




# req_url = "https://jsonplaceholder.typicode.com/posts"
#
# res = requests.get(url= req_url)
# print(res)
# # ls = [i for i in res if i["title"] <= 8]
# # print(ls)
#
# for data in res.json():
#     if len(data.get("title").split()) <= 8:
#         print(data)


# def sample_function(a,*args):
#     if (a==10):

# from url take all email id and store in a list
# import requests
# res_url = "https://jsonplaceholder.typicode.com/comments"
# res = requests.get(url= res_url,  params={
#                    "postId":4})
# print(res.json())
# list =[]
# for i in res.json():
#     list.append(i["email"])
#     print(list)
#
#

# wap to print op where e is > 2 times in names in post5
# import requests
# res_url = "https://jsonplaceholder.typicode.com/comments"
# res = requests.get(url=res_url, params={"postId" : "5"})
# op = [x for x in res.json() if x["name"].count('e') > 2]
# print(op)


#create resource --post
# import requests
# res_url = "https://jsonplaceholder.typicode.com/posts"
# sample_entry ={
#     "title":'voldormort',
#     "body": 'bar',
#     "userId": 1
# }
# string_sample = json.dumps(sample_entry)
# res = requests.post(url=res_url, data=string_sample , headers={
#     'content-type': 'application/json ; charset=UTF-8'
# })
# print(res)
# print(res.json())


#wap to print random op of 5
# import requests
# import json
# req_url = "https://api.publicapis.org/random"
# l=[]
# for i in range(5):
#     res = requests.get(url=req_url)
#     l.append(res.json())
#     print(l)
#
#

import requests
import json
# req_url = "https://jsonplaceholder.typicode.com/comments?postId=1"
# user_input = input("Please enter the postid\n")
# user_input_split = user_input.split(":")
# sample_param ={}
# sample_param[user_input_split[0]] = user_input_split[1]
# res = requests.get(req_url,params=sample_param)
# print(res.json())


request_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url=request_url,params={"postId": input("")})
va = (response.json())
print(va)