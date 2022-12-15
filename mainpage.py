import customtkinter
from PIL import Image

from functools import partial
class MainPage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent, width=900)

        self.controller = controller
        self.id = controller.id

        self.num_chapter = self.controller.player.current_chapter

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.create_widget()

    def create_widget(self):

        # The menu frame
        menu_frame = customtkinter.CTkFrame(self, width=30, fg_color="transparent")
        menu_frame.grid(rowspan=2, column=1, sticky="ns", pady=(5, 5))

        # menu acces
        i = customtkinter.CTkImage(light_image=Image.open("assets/home.png"),
                                   dark_image=Image.open("assets/home.png"),
                                   size=(50, 50))
        b = customtkinter.CTkButton(
            master=menu_frame,
            cursor="hand2",
            command=partial(self.controller.up_frame, 'WelcomePage'),
            image=i,
            text='',
            font=self.controller.choicefont,
            width=40,
            fg_color="transparent")
        b.grid(row=1, column=0, padx=20, pady=(20, 0))

        # backpack acces
        i = customtkinter.CTkImage(light_image=Image.open("assets/backpack2.png"),
                                          dark_image=Image.open("assets/backpack2.png"),
                                          size=(50, 50))
        b = customtkinter.CTkButton(
                    master=menu_frame,
                    cursor="hand2",
                    command=lambda: self.button_function(),
                    image=i,
                    text='',
                    font=self.controller.choicefont,
                    width=40,
                    fg_color="transparent")
        b.grid(row=2, column=0, padx=20, pady=(20, 0))

        # map acces
        i = customtkinter.CTkImage(light_image=Image.open("assets/mapicon3.png"),
                                   dark_image=Image.open("assets/mapicon3.png"),
                                   size=(50, 50))
        b = customtkinter.CTkButton(
            master=menu_frame,
            cursor="hand2",
            command=lambda: self.button_function(),
            image=i,
            text='',
            font=self.controller.choicefont,
            width=40,
            fg_color="transparent")
        b.grid(row=3, column=0, padx=20, pady=(20, 0))

        # rules acces
        i = customtkinter.CTkImage(light_image=Image.open("assets/livre2.png"),
                                   dark_image=Image.open("assets/livre2.png"),
                                   size=(50, 50))
        b = customtkinter.CTkButton(
            master=menu_frame,
            cursor="hand2",
            command=lambda: self.button_function(),
            image=i,
            text='',
            font=self.controller.choicefont,
            width=40,
            fg_color="transparent")
        b.grid(row=4, column=0, padx=20, pady=(20, 0))


        # the text frame
        text_frame = customtkinter.CTkFrame(self, width=800, fg_color="transparent")
        text_frame.grid(column=0, row=0, sticky="ew", padx=(5, 5), pady=(5, 5))
        text = self.controller.gd.get_textchapter(self.num_chapter)
        t = customtkinter.CTkLabel(master=text_frame,
                                   text=text, font=self.controller.textfont, height=200, wraplength=826)
        t.grid(row=0, column=0, sticky="ew", padx=20)
        # t.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # the choices frame
        choice_frame = customtkinter.CTkFrame(self, width=840, fg_color="transparent")
        choice_frame.grid(column=0, row=1, sticky="ew", padx=(5, 5), pady=(5, 5))
        for i in range(4):
            t = self.controller.gd.get_textchoice(self.num_chapter, i+1)
            if t != '':
                button = customtkinter.CTkButton(
                    master=choice_frame,
                    cursor="hand2",
                    command=lambda: self.button_function(),
                    text=t,
                    font=self.controller.choicefont,
                    height=50,
                    width=750)
                button.grid(row=i, column=0, padx=20, pady=(5, 5), sticky="ew")


    def button_function(self):
        print("button pressed")






