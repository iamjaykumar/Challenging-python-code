# def speak(str):
#     from win32com.client import Dispatch
#
#     speak = Dispatch("SAPI.SpVoice")
#
#     speak.Speak(str)
#
# if __name__ == '__main__':
#     speak("Speak for today..Lets begin ")
# import requests
# import json
# def speak(str):
#     from win32com.client import Dispatch
#
#     speak = Dispatch("SAPI.SpVoice")
#
#     speak.Speak(str)
#
# if __name__ == '__main__':
#     speak("Speak for today..Lets begin ")
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1d91e82a3b2f48c8b77a5eb6f1215075"
#     news = requests.get(url).text
#     news_dict = json.loads(news)
#     arts = news_dict['articles']
#     for article in arts:
#         speak(article['title'])
#         print(article['title'])
#         speak("Moving on to the next news ... Listen")
#     speak("Thanks for listening")