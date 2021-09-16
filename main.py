from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from time import strftime

root = Tk()
style = Style()
style.theme_use("classic")

root.title("pyClock")
root.configure(background='gainsboro')
root.resizable(width=False, height=False)

size = 50
fnt = "Arial"

mainmenu = Menu(root)
root.config(menu=mainmenu)


def exit_clock():
    root.quit()


def about():
    messagebox.showinfo("About", "Creators \n Evgeniy Keselev \n"
                                 "Igor Mihaylets\n"
                                 "Copyright ©2021, E. Kiselev")


def help_clock():
    messagebox.showinfo("Help", "My e-mail\n"
                        "kiselev-05@list.ru")


def time():
    string = strftime('%H: %M: %S')
    label.config(text=string)
    label.after(900, time)


def time2():
    string = strftime('%H: %M: %S %p')
    label.config(text=string)
    label.after(900, time2)


def time3():
    string = strftime('%C: %Y: %H: %M: %S')
    label.config(text=string)
    label.after(900, time3)


def license_menu():
    messagebox.showinfo("License", "Free to use everywhere and everytime, for everyone\n"
                                   "Copyright ©2021, E. Kiselev")


raise_chek = False


def raise_above():
    global raise_chek
    if raise_chek is False:
        root.attributes('-topmost', True)
        raise_chek = True

    else:
        root.attributes('-topmost', False)
        raise_chek = False


programmenu = Menu(mainmenu, tearoff=0)
programmenu.add_command(label="License", command=license_menu)
programmenu.add_command(label="About", command=about)
programmenu.add_command(label="Help", command=help_clock)
programmenu.add_separator()
programmenu.add_command(label="Raise", command=raise_above)
programmenu.add_separator()
programmenu.add_command(label="Exit", command=exit_clock)


mainmenu.add_cascade(label="Program",
                     menu=programmenu)

label = Label(root, font=(fnt, size), background="gainsboro", foreground="white")
label.pack()
time()
root.mainloop()
