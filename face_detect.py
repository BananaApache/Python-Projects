
import time
import cv2
from random import randrange
from colorama import Fore as F
import os
import datetime
from check_archie import check_archie_once
from check_news import check_news as news
import pyautogui as pg

class Detect:
    def __init__(self, sec):
        try:
            self.sec = int(sec) + 1
        except:
            print(F.LIGHTRED_EX + "Unknown argument for Detect()" + F.RESET)
            exit()
        if sec == 0:
            self.sec = 3600

    def valid_face(self, save=False, talk=False, say_what="") -> dict:
        'valid_face(self, save=False, talk=False, say_what="") -> dict\n.   @param Set save to True to save pictures when faces are undeteced\n.@param Set talk to True to say something if a face is detected\n.   @param Set say_what to string that will be read out loud when face is detected (only works if talk=True)'
        face_detected = {}
        true_count = 0
        false_count = 0

        for i in range(1, self.sec):
            face_data = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            webcam = cv2.VideoCapture(0)
            frame = webcam.read()[1]

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(gray_img)

            if str(type(face_coord)) == "<class 'numpy.ndarray'>" and face_coord[0][2] > 200:
                if talk:
                    os.system(f"say -v Daniel 'I see you'")
                    true_count += 1
                face_detected.update({
                    f"face_detect{i}": True
                })
                if true_count == 4:
                    os.system("say -v Daniel 'I still see you'")
                    true_count += 1
                if true_count == 7:
                    os.system("say -v Daniel 'Still the same face'")
                    true_count += 1
                if true_count == 11:
                    os.system(
                        "say -v Daniel 'I am getting tired of seeing the same face, goodbye'")
                    exit()
            else:
                face_detected.update({
                    f"face_detect{i}": False
                })
                if save is True:
                    os.system("rm -rf ./face_detect_errors/*")
                    try:
                        (x, y, w, h) = face_coord[0]
                        cv2.rectangle(frame, (x, y), (x + w, y + h),
                                      (0, 0, 255), 2)
                    except:
                        pass
                    cv2.imwrite(
                        f'./face_detect_errors/face_detect{i}.png', frame)
                if talk:
                    os.system("say -v Daniel 'No face detected'")
                    false_count += 1
                if false_count > 10:
                    os.system("say -v Daniel 'There are no faces, goodbye'")
                    exit()
                if true_count > 0 and false_count < 5:
                    os.system("say -v Daniel 'Where did you go'")
                    false_count += 1

        return face_detected

    def face_box(self):
        face_boxes = {}

        for i in range(1, self.sec):
            face_data = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            webcam = cv2.VideoCapture(0)
            frame = webcam.read()[1]

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(gray_img)

            for (x, y, w, h) in face_coord:
                if w < 200:
                    continue
                elif w > 200:
                    face_boxes.update({
                        f"face_detect{i}": [x, y, w, h]
                    })

        return face_boxes

    def draw_box(self):
        count = 0
        while True:
            face_boxes = {}

            face_data = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            webcam = cv2.VideoCapture(0)
            frame = webcam.read()[1]

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(gray_img)

            for (x, y, w, h) in face_coord:
                if w < 200:
                    continue
                elif w > 200:
                    face_boxes.update({
                        f"face_detect{count}": [x, y, w, h]
                    })

            for coords in face_boxes.values():
                cv2.rectangle(frame, (coords[0], coords[1]), (coords[0] +
                              coords[2], coords[1] + coords[3]), (0, 0, 255), 2)

            cv2.imshow('Face Detector', frame)
            cv2.waitKey(1)

            count += 1

    def wake_up(self):
        face_detected = {}
        greetings = ["Ahoy, matey", "Hello I come in peace", "Hello, governor", "Top of the morning to ya", "Wassup, homey",
                     "Whats good bruh", "ring ring ring, hello", "Hello hello! Whose there? Its me", "Yo! Wassup", "Whaddup bro", "Greetings and salutations, my man", "Yoooouhoooo! Toodle doo, toodle dum", "Hola paapi", "Good day, young man", "Bing bing! Hows it going", "Whats up with you, old soul"]
        wake_up_file = open("wake_up.txt", "a")

        for i in range(1, self.sec):
            face_data = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            webcam = cv2.VideoCapture(0)
            frame = webcam.read()[1]

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(gray_img)

            if str(type(face_coord)) == "<class 'numpy.ndarray'>" and face_coord[0][2] > 200:
                rand = randrange(0, 17)
                os.system(f"say -v Daniel '{greetings[rand]}'")
                face_detected.update({
                    f"face_detect{i}": True
                })
                wake_up_file.write("Daniel woke up at " + str(datetime.datetime.now().strftime(
                    "%I:%M %p")) + " on " + str(datetime.datetime.now().strftime("%A, %B %d, %Y") + "\n"))
                    
                is_there_hw = check_archie_once.check_archie_once()
                if is_there_hw:
                    os.system("say -v Daniel 'New homework has been sent to the email'")
                else:
                    os.system("say -v Daniel 'No new homework'")
                
                news_type = news.say_news("general")
                print(F.RED + f"\n{news_type}" + F.RESET)
                os.system(f"say -v Daniel for todays top news, {news_type}")
                exit()
            else:
                face_detected.update({
                    f"face_detect{i}": False
                })

        return face_detected

    def fun(self):
        false_count = 0
        for i in range(1, self.sec):
            face_data = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            webcam = cv2.VideoCapture(0)
            frame = webcam.read()[1]

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coord = face_data.detectMultiScale(gray_img)

            if str(type(face_coord)) == "<class 'numpy.ndarray'>" and face_coord[0][2] > 200:
                os.system("say -v Daniel oh no someone help me i see a bob, I am going to quit the program")
                pg.keyDown('command')
                pg.keyDown('tab')
                pg.keyUp('command')
                pg.keyUp('tab')
                exit()
            else:
                if false_count == 3:
                    os.system("say -v Daniel it is such a lovely day")
                if false_count == 8:
                    os.system("say -v Daniel It is so nice that there is no bobs around")
                false_count += 1
# detect = Detect(10)
# detect.face_box
# detect.valid_face
# detect.draw_box()


print(Detect(0).wake_up())
