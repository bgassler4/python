# Binary Search Algorithm
# Create a random list of numbers between 0 and 100
# with a difference of 2 between each number. Ask the
# user for a number between 0 and 100 to check whether
# their number is in the list. The programme should work
# like this. The programme will half the list of numbers and
# see whether the users number matches the middle element
# in the list. If they do not match, the programme will check
# which half the number lies in, and eliminate the other half.
# The search then continues on the remaining half, again checking
# whether the middle element in that half is equal to the user’s
# number. This process keeps on going until the programme finds the
# users number, or until the size of the subarray is 0, which means
# the users number isn't in the list.
import random

list_length = 10
num_min = 1
num_max = 100
num_list = []
completed = False


def get_random_number(a, b):
    return random.randint(a, b)


for i in range(list_length):
    num_list.append(get_random_number(num_min, num_max))

print(num_list)


def check_num(number):
    """
    "This function checks whether the number passed in is in the list"
    :param number:
    :return: bool if the number is in the array or not
    """
    global completed

    if number in num_list:
        print("Congratulations!")
        completed = True


def try_guess(num_list):
    try:
        user_guess = int(input("What is your next guess: "))
        check_num(user_guess)
    except ValueError:
        print("Input should be a whole number")


while not completed:
    try_guess(num_list)
