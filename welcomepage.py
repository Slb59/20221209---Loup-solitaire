import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from functools import partial

class WelcomePage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.id = controller.id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)



        self.create_widget()

    def create_widget(self):

        t = customtkinter.CTkLabel(master=self, text='Loup Solitaire', font=self.controller.titlefont)
        t.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        t = customtkinter.CTkLabel(master=self, text='Joueur actif : ', font=self.controller.textfont)
        t.grid(row=1, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text='Règles du jeu',
            font=self.controller.choicefont,
            corner_radius=10,
            height=50)
        button.grid(row=2, columnspan=2, padx=20, pady=(20, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text='Créer un nouveau profil',
            font=self.controller.choicefont,
            corner_radius=10,
            height=50)
        button.grid(row=3, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text='Charger un profil',
            font=self.controller.choicefont,
            corner_radius=10,
            height=50)
        button.grid(row=4, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        button = customtkinter.CTkButton(
            master=self,
            cursor="hand2",
            command=lambda: self.button_function(),
            text="Démarrer l'aventure",
            font=self.controller.choicefont,
            corner_radius=10,
            height=50)
        button.grid(row=5, columnspan=2, padx=20, pady=(0, 20), sticky="ew")


    def button_function(self):
        print("button pressed")

