import customtkinter

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
        menu_frame = customtkinter.CTkFrame(self, width=40)
        menu_frame.grid(rowspan=2, column=1, sticky="ns")
        t = customtkinter.CTkLabel(master=menu_frame, text='Menu', font=self.controller.textfont)
        t.grid(row=0, column=0, padx=20, pady=(20, 0))

        # the text frame
        text_frame = customtkinter.CTkFrame(self, width=900)
        text_frame.grid(column=0, row=0, sticky="ew", padx=(5, 5), pady=(5, 5))
        text = self.controller.gd.get_textchapter(self.num_chapter)
        t = customtkinter.CTkLabel(master=text_frame, text=text, font=self.controller.textfont, height=300)
        t.grid(row=0, column=0, sticky="ew", padx=5)

        # the choices frame
        choice_frame = customtkinter.CTkFrame(self, width=840)
        choice_frame.grid(column=0, row=1, sticky="ew")
        for i in range(4):
            t = self.controller.gd.get_textchoice(self.num_chapter, i+1)
            if t != '':
                button = customtkinter.CTkButton(
                    master=choice_frame,
                    cursor="hand2",
                    command=lambda: self.button_function(),
                    text=t,
                    font=self.controller.choicefont,
                    height=50)
                button.grid(row=i, column=0, padx=20, pady=(5, 5), sticky="ew")


    def button_function(self):
        print("button pressed")






