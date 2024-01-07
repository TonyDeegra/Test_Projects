# i = 5
# while i <= 15:
#     print( i )
#     i += 1
# print('end')

# i = 8
# while i <= 33:
#     if i % 2 != 0:
#         print( i )
#     i += 1

# a = int(input('Enter: '))
# while a != 0:
#     int(input('Enter: '))
#     print(a)

# a = 0
# while True:
#     s = int(input('Enter: '))
#     if s == 0:
#         break
#     else:
#         a += s
# print(a)

a = int(input('Enter: '))
s = a
while a != 0:
    a = int(input("Enter: "))
    s += a
    if a == 0:
        print(s)
