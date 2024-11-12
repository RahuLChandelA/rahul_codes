# questtion one
# def length(a):
#     return len(a)
    
# x = list([1,23,4,4,3,5])

# print(length(x))

# # question two

# def print_list(list):
#     x.sort()
#     for i in list:
#         print(i,end=" ")

# print_list(x)

# question three

# def fact(y):
#     ans=1
#     for i in range(1,y+1):
#         ans *= i
#     print(ans)

# fact(4)

# question four

# def convertor(m):
#     g = m*83
#     print(m,"USD =",g,"INR")

# convertor(2)

# def even_odd(x):
#     if x%2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_odd(4)
# even_odd(3)

                       ## recursion
# def show(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     show(n-1)

# show(7)

# def fact(x):
#     if x == 1 or x==0:
#         return 1
#     else:
#         return x * fact(x-1)

# print(fact(4))

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n+sum(n-1)

# print(sum(10))

a = list([1,2,3,4,5,6])

def print_list(b , i=0):
    if i == len(b):
        return
    print(b[i],end=" ")
    print_list(b,i+1)

print_list(a)