import tkinter
from tkinter import *
import settings


def create_game_window():
    main_window.destroy
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
    command=main_window.destroy
)

btnExit.place(x=50, y=120)

main_window.mainloop()
