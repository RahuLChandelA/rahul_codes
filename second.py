# escape characterss
# print('it\'s a beautiful day')
# print('we are from \'IIIt\' Nagpur')

# use of tab or "\t"
# print("My name is anuj. \t I am from haryana.")

# use of "\n"
# print("My name is anuj. \nI am from haryana.")


#  introduction to triple quotes
# used to store a multi line string
# x = '''first line
# second line 
# third line '''
# print(x)


# more to strings
# lower() : convert srting  in lower case
# upper() : convert srting in upper case
# capitilise() : convert first lettr of string in upper case
# title() : convert word letter of each word in uppper case
# swapcase() : convert upper to lover case and vice versa
# isdigit() : return true if all charac. are digits
# isalpha() : return true if all charac. are aplhabets
# isalnum() : return true if all charac. are aplabets ir digits
# strip() : return trimmed version of string
    # exam. x= "--python--" print(x.strip('x')) output will be "python"
# strip have two type: a) lstrip() b) rstrip()
# startswith() : 
# endswith() :
# count():
# index() :
# replace (x,y) : replaces x with y



# g,s,b = map(int,input().split())

# x = 0

# if g<5:
#     x = x + 5-g
# elif s<5:
#     x = x + 5-s
# elif b<5:
#     x = x + 5-b
    
# print(x)

# for _ in range(int(input())):
    
# n,x,y = map(int,input().split())
# s = input()
    
# x_1 = s.count("R")
# x_2 = s.count("L")
# y_1 = s.count("U")
# y_2 = s.count("D")

# a = x + x_1 - x_2
# b = y + y_1 - y_2
# print(x_1 , x_2 , y_1 , y_2)

# # time = abs(x-a) + abs(y-b)
    
    

# s = input()
# compressed_string = []
# count = 1

# for i in range(1,len(s)):
#     if s[i] == s[i-1]:
#         count+=1
#         if i == (len(s)-1):
#             compressed_string.append(s[-1]+ str(count))
#     else:
#         compressed_string.append(s[i-1]+str(count))
#         count = 1

# print(compressed_string)

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [1, 1, 2, 0, 0]
print(most_frequent(List))



    