# LOW = 1
# HIGH = 100

# def fizz_buzz(number:int) -> str:
#     """Return different strings dependend on input
#     If input is divisable by 3, return fizz
#     if input is divisable by 5, return buzz
#     if input is divisable by 3 or 5, return fizz buzz
#     else return int as str

#     Args:
#         number (`int`): A positive number between 1 and 100 inclusive

#     Returns:
#         `str`: Return a string based on user input
#     """

#     if number % 15 == 0:
#         return "fizz buzz"
#     if number % 3 == 0:
#         return "fizz"
#     if number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)

# # for i in range(LOW, HIGH +1):
# #     print("{}: {}".format(i, fizz_buzz(i)))

# # Call fizz_buzz() and print result
# # We need a variable to pass

# input("Play Fizz Bizz. Press ENTER to start: ")
# print()

# # Keep count
# next_number = 0 # initialise to 0
# while next_number < 99:
#     next_number +=1 # increase by 1 for each iteration
#     print(fizz_buzz(next_number))
#     next_number +=1
#     correct_answer = fizz_buzz(next_number)
#     players_answer = input("Your go: ")
#     if players_answer != correct_answer:
#         print("You lose, the correct answer was: {}".format(correct_answer))
#         break
# else:
#     print("Well done, you reached {}".format(next_number))