import customtkinter

from functools import partial

class WelcomePage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.id = controller.id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.player = self.controller.player

        self.create_widget()

    def create_widget(self):

        t = customtkinter.CTkLabel(master=self, text='Loup Solitaire', font=self.controller.titlefont)
        t.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        if self.player.name == '':
            t_actif_player = 'Pas de joueur actif'
        else:
            t_actif_player = f'Joueur actif : {self.player.name}, {self.player.title} de niveau {self.player.level}'
        t = customtkinter.CTkLabel(master=self, text=t_actif_player, font=self.controller.textfont)
        t.grid(row=1, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=partial(self.controller.up_frame, 'DisciplinePage'),
            text='Règles du jeu',
            font=self.controller.choicefont,
            height=50)
        button.grid(row=2, columnspan=2, padx=20, pady=(20, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text='Créer un nouveau profil',
            font=self.controller.choicefont,
            height=50)
        button.grid(row=3, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text='Charger un autre profil',
            font=self.controller.choicefont,
            height=50)
        button.grid(row=4, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=partial(self.controller.up_frame, 'MainPage'),
            text="Démarrer l'aventure",
            font=self.controller.choicefont,
            height=50)
        if self.player.name == '':
            button.configure(state="disabled")
        button.grid(row=5, columnspan=2, padx=20, pady=(0, 20), sticky="ew")


    def button_function(self):
        print("button pressed")

