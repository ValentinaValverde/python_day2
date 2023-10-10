import random

num = int(input("pick a number between 1 and 10. -> "))
magic_num = random.randint(1, 10)


def not_num():
    print("wrong number, please try again!")
    not_num = int(input("pick a number between 1 and 10. -> "))
    main(not_num)

def out_of_range():
    print("out of range, please try again!")
    num = int(input("pick a number between 1 and 10. -> "))
    main(num)


#main function
def main(num):
    if num not in range(1, 10):
        out_of_range()

    elif num != magic_num:
        not_num()
    
    else:
        print("this is the magic number: ", magic_num)
        print("ARE YOU A MIND READER???")

main(num)


#python3 conditionals.py 