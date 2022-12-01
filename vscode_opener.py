
import os
from tkinter import *
import sys
sys.path.append("/usr/local/lib/python3.10/site-packages")
import tkmacosx as tk

window = Tk()
window.geometry("1500x1000")
window.title("File Explorer")
window.attributes("-topmost", True)
window.config(bg="#63666A")


def open_f(fname):
    os.system(f"open 'vscode://file//Users/dli/{fname}'")
    # print("Would open /Users/dli/" + fname)
    exit()


def open_pyf(pyf_name):
    os.system(f"open 'vscode://file//Users/dli/{pyf_name}'")
    exit()


global btn_lst
btn_lst = []


def ls_downloads():
    global folder_btn
    o = os.popen("ls -ltr /Users/dli/Downloads | tail")
    count = 1
    for folder in o:
        folder = folder.split()
        folder = folder[len(folder)-1]
        folder_btn = tk.Button(window, text=folder, highlightbackground="#53666A", bg="#187bcd", fg="white",
                               command=lambda folder=folder: ls_subfolders(folder_name=f"Downloads/{folder}"))
        folder_btn.grid(row=count, column=3)
        btn_lst.append(folder_btn)
        count += 2
        btn_lst.append(folder_btn)


def ls_subfolders(folder_name):
    global open_btn
    global new_folder_btn
    global f
    global folder_btn
    global subfolder_btn
    f = folder_name
    # o = os.popen(f"ls -l /Users/dli/{folder_name} | grep '^d\|.py'").read().split("\n")
    o = os.popen(f"ls /Users/dli/{folder_name}").read().split("\n")
    count = 3
    for subfolder in o:
        # subfolder = subfolder[51:]
        # print(subfolder)
        if str(subfolder)[len(str(subfolder)) - 3:] != ".py":
            subfolder_btn = tk.Button(
                window, text=subfolder, fg="white", highlightbackground="#53666A", bg="#187bcd", command=lambda subfolder=subfolder: ls_subfolders(f"{folder_name}/{subfolder}"))
            subfolder_btn.grid(row=count, column=2 +
                               len(f"{folder_name}/{subfolder}".split("/")))
            # print(f"{folder_name}/{subfolder}")
        else:
            pyf = subfolder
            python_btn = tk.Button(window, text=subfolder, highlightbackground="#53666A", bg="#187bcd", fg="white", command=lambda pyf=pyf: open_pyf(
                f"{folder_name}/{subfolder}{pyf}"))
            python_btn.grid(row=count, column=2 +
                            len(f"{folder_name}/{subfolder}".split("/")))
        btn_lst.append(subfolder_btn)
        count += 2
    col = 2+len(f"{folder_name}/{subfolder}".split("/"))
    open_btn = tk.Button(window, text="Open", highlightbackground="#53666A", bg="#187bcd", fg="white",
                         command=lambda folder_name=folder_name: open_f(folder_name))
    open_btn.grid(row=1, column=0)
    new_folder_btn = tk.Button(window, text="New Folder", fg="white", bg="#03AC13", highlightbackground="#53666A",
                               command=lambda folder_name=folder_name: new_f(folder_name))
    new_folder_btn.grid(row=2, column=0)


def get_inp():
    global inp
    inp = dir_name_inp.get()
    print(f'mkdir /Users/dli/{f}/{inp}')
    os.system(f'mkdir /Users/dli/{f}/{inp}')


def new_f(folder_dir):
    global dir_name_inp
    # var = IntVar()
    dir_name_inp = Entry(window)
    dir_name_inp.grid(row=4, column=0)
    # make_folder_btn = tk.Button(window, text="Make", command=lambda: [get_inp(), var.set(1)])
    make_folder_btn = tk.Button(window, text="Make", command=get_inp)
    make_folder_btn.grid(row=5, column=0)
    # make_folder_btn.wait_variable(var)
    # print(f'mkdir {dir_name_inp} /Users/dli/{folder_dir}')
    # os.system(f'mkdir {inp} /Users/dli/{folder_dir}')


def ls():
    global folder_btn
    global subfolder_btn
    o = os.popen("ls -l /Users/dli/ | grep '^d\|.py'").read().split("\n")
    count = 1
    for folder in o:
        folder = folder[51:]
        folder_btn = tk.Button(window, text=folder, highlightbackground="#53666A", bg="#187bcd", fg="white",
                               command=lambda folder=folder: ls_subfolders(folder_name=folder))
        folder_btn.grid(row=count, column=2)
        if str(folder) == "Downloads":
            downloadfolder_btn = tk.Button(window, text="Downloads", fg="white",
                                   highlightbackground="#53666A", bg="#187bcd", command=ls_downloads)
            downloadfolder_btn.grid(row=count, column=2)
            btn_lst.append(downloadfolder_btn)
        # print(folder)
        btn_lst.append(folder_btn)
        count += 2


def reload():
    for btn in btn_lst:
        btn.destroy()


reload_btn = tk.Button(window, text="Reload", command=reload)
reload_btn.grid(row=7, column=0)
new_folder_btn = tk.Button(window, text="New Folder", fg="white", bg="#03AC13", highlightbackground="#53666A",
                           command=lambda: new_f(""), state=DISABLED)
new_folder_btn.grid(row=2, column=0)
open_btn = tk.Button(window, text="Open", fg="white", bg="#187bcd", highlightbackground="#53666A",
                     command=lambda: open_f(""), state=DISABLED)
open_btn.grid(row=1, column=0)
exit_btn = tk.Button(window, text="Exit", bg="#D21404", fg="white",
                     highlightbackground="#53666A", command=window.quit)
exit_btn.grid(row=8, column=0)
show_files = tk.Button(window, text="Show Files",
                       highlightbackground="#53666A", command=ls)
show_files.grid(row=0, column=0)

window.mainloop()
