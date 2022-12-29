import random
#
# # def play():
# #     user = input("What's your choise ? 'r' for rock and 'p' for paper  and 's ' for scissors\n")
# #     computer = random.choice(['s', 'p', 'r'])
# #
# #     if user == computer:
# #         return "It's about Tie :"
# #     if is_win(user, computer):
# #         return "you won !"
# #
# #     return "you lost !"
# #
# # def is_win(player, unplayer):
# #     if (player == 'r' and unplayer == 's') or (player == 's' and unplayer == 'p') or \
# #                 (player == 'p' and unplayer == 'r'):
# #         return True
# #
# #
# # print(play())
#
# def play():
#     user = input("'s' for snake and 'w' for water and 'g' for gun\n")
#     computer = random.choice(['s','w', 'g'])
#     if user == computer:
#         return "It's about Tie"
#     elif to_win(user, computer):
#         return "you won"
#     return 'you lost'
#
# def to_win(player, opponent):
#     if (player == 's' and opponent == 'w') or (player == 'w' and opponent == 'g') or (player == 'g' and opponent == 's'):
#         return True
# print(play())