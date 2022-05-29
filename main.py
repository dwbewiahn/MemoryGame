from tkinter import *
import settings
import sys

main_window = Tk()

# Main window Settings
main_window.title('Memory Card Game')
main_window.configure(bg=settings.MAIN_COLOR)
main_window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
main_window.resizable(False, False)

btnStart = Button(
    main_window,
    width=20,
    height=3,
    text='START'
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
