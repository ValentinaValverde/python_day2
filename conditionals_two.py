import random

num = int(input("pick a number between 1 and 10. -> "))
print(num)
magic_num = random.randint(1, 10)


def not_num():
    print("wrong number, please try again!")
    num = int(input("pick a number between 1 and 10. -> "))
    main(num)

def main(num):
    while num in range(1, 10) and num != magic_num:
        not_num()
        break


main(num) 
print("done!")
