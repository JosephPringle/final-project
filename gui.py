from tkinter import *
from tkinter import Frame

import compute

class GUI:

    def __init__(self, window):
        self.window = window

        self.cookie = 0
        self.sandwich = 0
        self.water = 0

        self.frame_continue_or_quit = Frame(self.window)
        self.label_question = Label(self.frame_continue_or_quit, text='select an item to add to the cart. Press finish when done shopping')
        self.frame_continue_or_quit.pack(anchor='w', pady=5)

        self.frame_window_shop = Frame(self.window)
        self.label_shop = Label(self.frame_window_shop, text='----cart menu---- \n '
                                                             '1: Cookie - $1.50 \n '
                                                             '2: Sandwich - $4.00 \n '
                                                             '3: Water - $1.00\n')
        self.label_option = Label(self.frame_window_shop, text='Please add one of the following to the cart.')
        self.label_shop.pack()
        self.label_option.pack()
        self.frame_window_shop.pack()

        self.radio_frame = Frame(self.window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_cookie = Radiobutton(self.radio_frame, text='cookie', variable=self.radio_1, value=1)
        self.radio_sandwich = Radiobutton(self.radio_frame, text='sandwich', variable=self.radio_1, value=2)
        self.radio_water = Radiobutton(self.radio_frame, text='water', variable=self.radio_1, value=3)
        self.radio_cookie.pack(side='left')
        self.radio_sandwich.pack(side='left')
        self.radio_water.pack(side='left')
        self.radio_frame.pack()

        self.frame_add = Frame(self.window)
        self.label_add_item = Label(self.frame_add)
        self.label_add_item.pack(pady=10)
        self.frame_add.pack()

        self.frame_total_cost = Frame(self.window)
        self.label_total_cost = Label(self.frame_total_cost)
        self.label_total_cost.pack()
        self.frame_total_cost.pack()

        self.frame_calculate = Frame(self.window)
        self.button_calculate = Button(self.frame_calculate, text='Add', command=self.calculate)
        self.button_calculate.pack()
        self.frame_calculate.pack()

        self.frame_results = Frame(self.window)
        self.button_results = Button(self.frame_results, text='Finish', command=self.result)
        self.button_results.pack()
        self.frame_results.pack()

    def calculate(self):
        item = self.radio_1.get()
        if item == 1:
            self.cookie += 1
            self.label_add_item.config(text='1 cookie added')
        elif item == 2:
            self.sandwich += 1
            self.label_add_item.config(text='1 sandwich added')
        elif item == 3:
            self.water += 1
            self.label_add_item.config(text='1 water added')
        print(self.sandwich, self.water, self.cookie)

        self.radio_1.set(0)

    def result(self):

        if self.cookie == 0 and self.sandwich == 0 and self.water == 0:
            self.label_add_item.config(text='please add one item to the cart before pressing finish.')
        cookie_price = compute.cookie(self.cookie)
        sandwich_price = compute.sandwich(self.sandwich)
        water_price = compute.water(self.water)
        total_price = cookie_price + sandwich_price + water_price

        self.label_total_cost.config(text='-----------------\n'
                                            f'{self.cookie} - cookies = ${cookie_price:.2f}\n'
                                            f'{self.sandwich} - sandwiches = ${sandwich_price:.2f}\n'
                                            f'{self.water} - water = ${water_price:.2f}\n'
                                            f'total cost = ${total_price:.2f}')
        self.label_add_item.config(text='')




