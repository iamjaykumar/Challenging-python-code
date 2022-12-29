# from pygame import mixer
# from datetime import datetime
# from time import time
# def music_on_loop(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break
# def log_now(msg):
#     with open("mylog.txt" , "a") as f:
#         f.write(f"{msg}  {datetime} \n")
# if __name__ == '__main__':
#     init_water = time()
#     init_exercise = time()
#     init_eyes = time()
#     watersec = 2
#     exercisesec = 5
#     eyesec = 10
#     while True:
#         if time() - init_water > watersec:
#             print("Water drinking time . Enter 'drank ' to stop the alarm ")
#             music_on_loop("water.mp3", "drank")
#             init_water = time()
#             log_now("Drank water at ")
#
#         if time() - init_exercise > exercisesec:
#             print("Physical activity  time . Enter 'doneex ' to stop the alarm ")
#             music_on_loop("exercise.mp3", "doneex")
#             init_exercise = time()
#             log_now("Pysical activity  at ")
#
#
#         if time() - init_eyes > eyesec:
#             print("Eyes relaxing  time . Enter 'doneeyes ' to stop the alarm ")
#             music_on_loop("eyes.mp3", "doneeyes")
#             init_eyes = time()
#             log_now("Done eyes relaxing at ")
#             # if you want to continue this loop so don't need to use break statement
#             break
#