# with open("test.txt", "w", encoding='utf-8') as file:
#     file.write("Привет, файл!\n")

# with open("Test.txt", "r", encoding="utf-8") as file:
#     x = file.readline()
#     print(x)

# a = 0
# with open("numbers.txt", "w") as file:
#     for i in range(1,11):
#         file.write(str(i) + "\n")
# with open("numbers.txt", "r") as file:
#     x = file.readlines()
#     for i in x:
#         b = int(i)
#         a = a + b
#     print(a)

# with open("user_text.txt", "w", encoding = "utf-8") as file:
#     a = 0
#     while True:
#         print("Введите строку или 'выход' для выхода")
#         a = input()
#         if a != "выход":
#             file.write(a + "\n")
#         else:
#             break
# with open("user_text.txt", "r", encoding= "utf-8") as file:
#     x = file.readlines()
#     for i in x:
#         a = len(i)
#         if a > 5:
#             print(i)
#         else:
#             a = a
        
# with open("data.txt", "r", encoding="utf-8") as file:
#     x = file.readlines()
#     a = len(x)
#     print(a)


# with open("text.txt", "r", encoding= "utf-8") as file:
#     x = file.read()
#     a = x.split()
#     b = len(a)
#     print(b)

# with open('log.txt', "a", encoding= "utf-8") as file:
#     a = 0
#     while True:
#         print("Введите строку или 'выход' для выхода")
#         a = input()
#         if a != "выход":
#             file.write(a + "\n")
#         else:
#             break
# with open("log.txt", "r", encoding= "utf-8") as file:
#     f = file.readlines()
#     for i in f:
#         print(i)

# with open("num.txt", "r") as file:
#     a = file.read()
#     b = a.split()
#     x = 0
    
#     for i in b:
#         g = int(i)
#         if g > x:
#             x = g
#         else:
#             x = x
#     y = min(b)
#     print(f"Мамксимальное: {x}")
#     print(f"Минимальное: {y}")

# with open("text.txt", "r", encoding= "utf-8") as file:
#     x = file.readlines()
# with open("text2.txt", "w", encoding= "utf-8") as file:
#     file.writelines(x)

# with open("text.txt", "r", encoding= "utf-8") as file:
#     x = file.readlines()

# with open("text3.txt", "w", encoding= "utf-8") as file:
#      a = map(str.upper, x)
#      file.writelines(a)

import json
with open("student.json", "w", encoding= "utf-8") as file:
    file.write("name: Tom age: 18 city: Omsk")

    
with open("student.json", "r", encoding= "utf-8") as file:
    a = file.read()
    print(a)    
    