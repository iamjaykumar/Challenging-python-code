# import random
#
# # def guess(x):
# #     random_number = random.randint(1, x)
# #     guess = 0
# #     while guess != random_number:
# #         guess = int(input(f'Guess a number between 1 and {x}: '))
# #         if guess < random_number:
# #             print('Sorry ! , try again . Too low')
# #         elif guess > random_number:
# #             print('Sorry ! , try again . Too high ')
# #     print(f"Yah! congrates you are guess the right number{random_number} correctly .")
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low , high)
#         else:
#             guess = low
#         feedback = input(f'Is {guess} too high (H), too low (L) , or correct (c)')
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback  == 'l':
#             low = guess + 1
#
#     print(f'yay ! The computer guess your number ! {guess} correctly' )
#
# computer_guess(100)
