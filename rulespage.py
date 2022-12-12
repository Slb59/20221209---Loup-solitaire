import customtkinter

class RulesPage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent, width=900)

        self.controller = controller
        self.id = controller.id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)



        self.create_widget()

    def create_widget(self):

        pass

