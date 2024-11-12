# f = open('demo.txt', 'r')
# new = f.read(5)
# print(new)
# print(type(new))
# f.close()


# f = open('sample.txt' , 'a')
# f.write("this is the anuj")
# f.close()

# g = open("sample.txt" , "r")
# new = g.read()
# print(new)
# g.close()

# f=  open("demo.txt" , "r+")

# f.write("abc")

# new = f.read()
# print(new)

# f.close()

# g =  open("demo.txt" , "r+")

# new_1 = g.read()
# print(new_1)
# g.close()


##   better way or syntax

# with open("demo.txt","r") as f:
#     this = f.read()
#     print(this)

# with open("demo.txt","w") as f:
#     f.write("anuj jakhar")

# with open("practice.txt" , "w") as f:
#     f.write("hi everyone\nwe are learning File I/O\n")
#     f.write("using java.\nI like programming in java")

# with open("practice.txt","r") as f:
#     new_2 =  f.read()

# new_data = new_2.replace("java" , "python")

# with open("practice.txt","w") as f:
#     f.write(new_data) 

# with open("practice.txt","r") as f:
#     new_data = f.read()
#     if new_data.find("learning") != -1:
#         print("FOUND")
#     else:
#         print("NOT FOUND")

# data = True
# count = 0
# with open("practice.txt","r") as f:
#     while data:
#         new_data = f.readline()
#         if new_data.find("learning") != -1:
#             data = False
#         else:
#             count+=1
    
#     print(count+1)

# 1,2,76,84,90,101

# with open("practice.txt","w") as f:
#     f.write("1,2,76,84,90,101")

# count=0
# with open("practice.txt","r") as f:
#     data = f.read()
#     num =""
#     a = list()
#     for i in range(len(data)):
#         if data[i] == ",":
#             a.append(int(num))
#             num = ""
#         else:
#             num += data[i]
    
#     count = 0
#     for i in range(len(a)):
#         if a[i]%2 == 0:
#             count+=1
    
#     print(count)




            

            









