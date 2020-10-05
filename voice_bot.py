import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 as p
from datetime import datetime
import time
import datetime
import random

#Создаем лог
chat_log = [['SESSION_ID', 'DATE', 'AUTHOR', 'TEXT', 'AUDIO_NUM']]
#Узнаем номер сессии
i = 1
exit = 0
while exit == 0:
    session_id = str(i)
    if session_id not in os.listdir():
        os.mkdir(session_id)
        exit = 1
    else:
        i = i + 1
#Первое сообщение пишет bot
author = 'Bot'
text = 'Привет! Чем я могу вам помочь?'

#Добавляем данные к логу с помощью этой процедуры
def log_me(author, text, audio): 
    now = datetime.datetime.now()
    i = 1
    exit = 0
    while exit == 0:
        audio_num = str(i)+'.wav'
        if audio_num not in os.listdir(session_id):
            exit = 1
        else:
            i = i + 1
    os.chdir(session_id)
    with open(audio_num , "wb") as file:
        file.write(audio.get_wav_data())
    chat_log.append([now.strftime("%Y-%m-%d %H:%M:%S"), author, text, audio_num])
    
#Настройка микрофона    
def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        #Бот ожидает нашего голоса
        print('Bot: ...')
        #Небольшая задержка в записи
        rec.pause_threshold = 1
        #Удаление фонового шума с записи
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        #Распознание теста с помощью сервиса GOOGLE
        text = rec.recognize_google(audio, language="ru-RU").lower()
        #Вывод сказанного текста на экран
        print('Вы:  ' + text[0].upper() + text[1:])
        log_me('User', text, audio)
    #Если не распознался тест из аудио
    except sr.UnknownValueError:
        text = 'Не понимаю. Повторите.'
        print('Bot: ' + text)
        talk(text)
        #Начинаем заново слушать
        text = command()
        log_me('Bot', text, , Null)
    return text

#Произношение words
def talk(words):
    engine.say(words)
    engine.runAndWait()
    
#Тут расписаны действия, которые будут выполнятся при наличии некоторых словосочетаний
def makeSomething(text):
    if 'открой сайт' in text:
        print('Bot: Открываю сайт NewTechAudit.')
        talk('Открываю сайт NewTechAudit.')
        log_me('Bot','Открываю сайт NewTechAudit.', Null)
        webbrowser.open('https://newtechaudit.ru/') 
    elif 'произнеси' in text or 'скажи' in text or 'повтори' in text:
        print('Bot: ' + text[10].upper() + text[11:])
        talk(text[10:])
        log_me('Bot', text[10].upper() + text[11:] , Null)
   #Ответ на вопрос
    elif 'своё имя' in text or 'как тебя зовут' in text or 'назови себя' in text:
        print('Bot: Меня зовут Bot.')
        talk('Меня зовут Bot')
        log_me('Bot', 'Меня зовут Bot', Null)
        #Определение случайного числа
    elif 'случайное число' in text:
        ot=text.find('от')
        do=text.find('до')
        f_num=int(text[ot+3:do-1])
        l_num=int(text[do+3:])
        r=str(random.randint(f_num, l_num))
        print('Bot: ' + r)
        talk(r)
        log_me('Bot', r, Null)
    #Завершение программы
    elif 'пока' in text or 'до свидания' in text:
        print('Bot: До свидания!')
        talk('До свидания')
        log_me('Bot', 'Конец сессии', Null)
        os.chdir(session_id)
        log_file = open( session_id + ".txt", "w")
        for row in chat_log:
            np.savetxt(log_file, row)
        log_file.close()
        sys.exit()

#Бесконечный цикл для работы
#while True:
#    makeSomething(command())
