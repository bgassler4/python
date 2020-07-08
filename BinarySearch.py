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
import math

initial_list_length = 10
num_min = 1
num_max = 100
num_list = []
count = 0
completed = False


def get_random_number(a, b):
    return random.randint(a, b)


element = get_random_number(num_min, num_max);
for i in range(initial_list_length):
    num_list.append(element)
    element += 2

print(num_list)


def check_num(number_list, number):
    """
    "This function checks whether the number passed in is in the list"
    :param number_list: the list of numbers to check
    :param number: check whether this number is in the list
    """
    global completed
    if len(number_list) == 1:
        if number_list[0] != number:
            complete_game(False, count)
            return
        else:
            complete_game(True, count)
            return
    half = len(number_list) // 2
    # check if the middle element is equal to the number guessed
    if number_list[half] == number:
        complete_game(True, count)


def complete_game(was_successful, count):
    global completed
    if was_successful:
        print("Success! \nYour number was in the list and it took {0} binary recursions to find it.".format(count))
    else:
        print("Failure! \nYour number was not in the list and {0} binary recursions were completed.".format(count))

    completed = True


def split_list(a_list):
    """
    :param a_list: the list to split
    :return: use floor division to split the list into 2 down the middle
    """
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def try_guess(num_list, user_guess):
    global count
    """
    recursively split an array until the users guess is the middle element of the array
    or the binary search determines that the users guess is not in the array
    :param num_list:
    :return: 
    """
    check_num(num_list, user_guess)
    if not completed:
        lower, higher = split_list(num_list)
        # if guess is lower than the first number in the higher list, use the lower list
        # else use the higher list
        if user_guess < higher[0]:
            count += 1
            try_guess(lower, user_guess)
        else:
            count += 1
            try_guess(higher, user_guess)


def run_program():
    while not completed:
        try:
            user_guess = int(input("What is your guess: "))
            try_guess(num_list, user_guess)
        except ValueError:
            print("Input should be a whole number")



run_program()

