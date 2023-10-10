
#part 1 - completed
# nums = [1, 2, 3, 4, 5, 99, 2600, 300]
# reversed_nums = list(reversed(nums))

# print("nums:", nums)
# print("reversed_nums", reversed_nums)



#part 2 - incomplete
# name = input("please type your name -> ")
# empty = []
# counter = 0

# while counter < len(name):
#     # print(name[counter])
#     empty.append(name[counter])
#     counter = counter + 1

# reversed_list = list(reversed(empty))

# print("reversed name:", "".join(reversed_list))



#part 3 - completed
new_list = ["hyungwon", "I.M.", "minhyuk", "shownu", "wonho", "joohooney", "kihyun" ]
print("before function:", new_list)

def new_func():
    if "wonho" in new_list:
        new_list.remove("wonho")
        print("after function:", new_list)
    else:
        new_list.append("wonho")
        print("after function:", new_list)

new_func()