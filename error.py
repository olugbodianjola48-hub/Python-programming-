import random


def my_function():
    for i in range(1, 20):
        if i ==20:
            print("you have reached the last number")

my_function()
#
# 2- REPRODUCE THE BUG
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = [1, 6]
print(dice_images[ dice_num[0] ])
#
# 3- PLAY COMPUTER
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("you are a millennial.")
elif year > 1994:
    print("you are a Gen Z.")

# 4
try:
    age = int(input("How  old are you?"))
except ValueError:
    print("You have typed in an invalid number. please try again with a numerical response such as 15.")
    age = int(input("How  old are you?"))

if age > 18:
    print(f"you can drive at age {age}")

# 6 - DEBUGGER
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,5,8,13])