import tkinter as tk
import customtkinter

from welcomepage import WelcomePage
from rulespage import RulesPage
from mainpage import MainPage
from playerpage import PlayerPage

from player import Player
from gamedata import GameData

class MainFrame(customtkinter.CTk):

    def __init__(self, *args, **kwargs):

        customtkinter.CTk.__init__(self, *args, **kwargs)

        # main data of game
        self.gd = GameData()
        self.gd.print()
        print('')
        self.player = Player()
        self.player.loadfile(self.gd.last_game())
        self.player.print()

        # main appearance of game
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("assets/theme/loup.json")

        self.titlefont = customtkinter.CTkFont(family="Raleway-Light", size=40, weight="bold", slant='roman')
        self.textfont = customtkinter.CTkFont(family="Raleway-Light", size=14, weight="normal", slant='roman')
        self.choicefont = customtkinter.CTkFont(family="Raleway-Light", size=16, weight="bold", slant='roman')
        self.title("Loup solitaire")
        self.geometry("950x600+300+150")
        self.minsize(300, 200)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        container = customtkinter.CTkFrame(
            master=self,
            corner_radius=10)
        container.pack(side="top", fill="both", expand=True)

        self.id = tk.StringVar()
        self.id.set('Loup solitaire')

        # load the frames
        self.listening = {}

        for F in (WelcomePage, RulesPage, MainPage, PlayerPage):
            frame = F(parent=container, controller=self)
            page_name = F.__name__
            self.listening[page_name] = frame
            frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 20), sticky="nsew")

        # call the welcome page
        self.up_frame('WelcomePage')

    def up_frame(self, page_name):
        page = self.listening[page_name]
        page.tkraise()

