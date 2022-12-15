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
        menu_frame = customtkinter.CTkFrame(self, width=60)
        menu_frame.grid(rowspan=2, column=1, sticky="ns")
        t = customtkinter.CTkLabel(master=menu_frame, text='Menu', font=self.controller.textfont)
        t.grid(row=0, column=0, padx=20, pady=(20, 0))

        # the text frame
        text_frame = customtkinter.CTkFrame(self, width=840)
        text_frame.grid(column=0, row=0, sticky="ew")

        # the choices frame
        choice_frame = customtkinter.CTkFrame(self, width=840)
        choice_frame.grid(column=0, row=1, sticky="ew")
        t = customtkinter.CTkLabel(master=choice_frame, text='choix', font=self.controller.textfont)
        t.grid(row=0, column=0, padx=20, pady=(20, 0))

        # the text frame
        text = self.controller.gd.chapter(self.num_chapter)
        t = customtkinter.CTkLabel(master=text_frame, text='text', font=self.controller.textfont)
        t.grid(row=0, column=0, padx=20, pady=(20, 0))



