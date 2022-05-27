from tkinter import *
import settings

main_window = Tk()

# Main window Settings
main_window.title('Memory Card Game')
main_window.configure(bg=settings.MAIN_COLOR)
main_window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
main_window.resizable(False, False)

main_window.mainloop()
