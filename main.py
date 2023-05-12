from gui import *


def main():
    window = Tk()
    window.title('Final project')
    window.geometry('500x400')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()