

import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore
import time as t
import smtplib
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

login_data = {"login_name": os.getenv("archie_username"),
              "passwd": os.getenv("archie_password"), "submit": "Login"}
url = "https://sis.archimedean.org/sis/default.php"

with requests.Session() as s:
    r = s.post(url, data=login_data)
    soup = bs(r.content, 'html.parser')
    # print(soup.prettify())
    hw_url = "https://sis.archimedean.org/sis/course_wall.php"
    r = s.get(hw_url)
    soup = bs(r.content, 'html.parser')

html_hw_lst = soup.findAll('td', nowrap='nowrap')
html_duedate_lst = soup.findAll('td', nowrap='nowrap')
html_teacher_lst = soup.findAll('td', nowrap='nowrap')
duedate_lst_unf = []
hw_lst = []
teacher_lst = []
duedate_lst = []

for duedate in html_duedate_lst:
    duedate.findNext('td')
    duedate = duedate.findNext('td')
    duedate = duedate.findNext('td')
    duedate = duedate.findNext('td')
    duedate_lst_unf.append(duedate.get_text())

for date_f in duedate_lst_unf:
    date_f = date_f.split("-")
    duedate_lst.append(str(date_f[1]) + "/" +
                       str(date_f[2] + "/" + str(date_f[0])))

for hw in html_hw_lst:
    hw_lst.append(hw.get_text())

for teacher in html_teacher_lst:
    teacher = teacher.findNext('td')
    teacher = teacher.findNext('td')
    teacher = teacher.findNext('td')
    teacher = teacher.findNext('td')
    teacher = teacher.findNext('td')
    teacher_lst.append(teacher.get_text())

file_hw = open(
    "/Users/dli/Documents/python_proj/archie/homework_file.txt", "r")

check_prev = ''
check_prev += ''.join(hw_lst)

hw_str = file_hw.read()

if hw_str == check_prev:
    print("\n" + Fore.GREEN + "No changes in homework" + Fore.RESET + "\n")
else:
    print("New Homework")
    print("\n" + Fore.CYAN + "Changes in homework detected" + Fore.RESET)
    print("\n" + Fore.GREEN + "Sending mail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('archimedean.mailer@gmail.com',
                 os.getenv("email_api_key"))

    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%-I:%M %p")

    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%B %d")

    homework = ' '.join(hw_lst)

    homework = ''

    for i in range(len(hw_lst)):
        homework += '' + \
            hw_lst[i] + " for " + teacher_lst[i] + \
            " is due on " + duedate_lst[i] + "\n\n"

    mail = 'Subject: {}\n\n{}'.format(
        "New Archie HW | " + str(current_date) + " " + str(current_time), homework)

    server.sendmail('anotheroneofmyemailacc@gmail.com',
                    'dabbingshrekbru@gmail.com', mail)
    print("\n" + Fore.RED + "Mail sent!\n" + Fore.RESET)

    print(Fore.YELLOW + "File written:" + Fore.RESET)

    for i in range(len(hw_lst)):
        print(Fore.GREEN + hw_lst[i] + Fore.RESET + " for " + Fore.BLUE + teacher_lst[i] +
              Fore.RESET + " is due at " + Fore.YELLOW + duedate_lst[i] + Fore.RESET)

file_hw = open(
    "/Users/dli/Documents/python_proj/archie/homework_file.txt", "w")

for write in hw_lst:
    file_hw.write(write)

file_hw = open(
    "/Users/dli/Documents/python_proj/archie/homework_file.txt", "r")

# t.sleep(1800)

# hour += 1
