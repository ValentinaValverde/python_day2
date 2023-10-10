#part 1 - completed

# start_num = int(input("please type a starting number -> "))
# end_num = int(input("please type a ending number -> "))


# if start_num > end_num:
#     print("sorry, you can't do that! try again")
#     start_num = int(input("please type a starting number -> "))
#     end_num = int(input("please type a ending number -> "))

# for x in range(start_num, end_num):
#     print(x)



#this is a loop that increments by more than 1:
# for x in range(start_num, end_num, 3):
#     print(x)



#part 2 - pending

new_string = "mother trucker"
counter = 0

while counter < len(new_string):
    if counter % 2 == 0 and new_string[counter] != " ":
        print(new_string[counter])

    counter = counter + 1