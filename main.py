import tkinter
from tkinter import *
import settings
import sys


def create_game_window():
    game_window = tkinter.Toplevel()
    game_window.title('Memory Card Game')
    game_window.configure(bg=settings.MAIN_COLOR)
    game_window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    game_window.resizable(False, False)


main_window = Tk()

# Main window Settings
main_window.title('Memory Card Game')
main_window.configure(bg=settings.MAIN_COLOR)
main_window.geometry('600x600')
main_window.resizable(False, False)

btnStart = Button(
    main_window,
    width=20,
    height=3,
    text='START',
    command=create_game_window
)

btnStart.place(x=50, y=50)

btnExit = Button(
    main_window,
    width=20,
    height=3,
    text='EXIT',
)

btnExit.place(x=50, y=120)

main_window.mainloop()
