#part 1


start_num = int(input("please type a starting number -> "))
end_num = int(input("please type a ending number -> "))


if start_num > end_num:
    print("sorry, you can't do that! try again")
    start_num = int(input("please type a starting number -> "))
    end_num = int(input("please type a ending number -> "))

for x in range(start_num, end_num):
    print(x)



#this is a loop that increments by more than 1:
# for x in range(start_num, end_num, 3):
#     print(x)