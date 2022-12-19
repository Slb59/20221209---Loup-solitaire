import customtkinter
from PIL import Image

from functools import partial

class PlayerPage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent, width=900)

        self.controller = controller
        self.id = controller.id

        self.player = self.controller.player

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.create_widget()

    def create_widget(self):

        # description : name, title, level, state
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=0, columnspan=4, sticky="ew", pady=(5, 5))
        frame.grid_columnconfigure(0, weight=1)
        text = f'{self.player.name}, {self.player.title} de niveau {self.player.level} - {self.player.state}'

        t = customtkinter.CTkLabel(master=frame,
                                   text=text, font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20)

        # menu acces
        i = customtkinter.CTkImage(light_image=Image.open("assets/home.png"),
                                   dark_image=Image.open("assets/home.png"),
                                   size=(50, 50))
        b = customtkinter.CTkButton(
            master=frame,
            cursor="hand2",
            command=partial(self.controller.up_frame, 'MainPage'),
            image=i,
            text='',
            font=self.controller.choicefont,
            fg_color="transparent")
        b.grid(row=0, column=1, padx=20)

        # last chapter
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=1, columnspan=4, sticky="ew", pady=(5, 5))
        frame.grid_columnconfigure(0, weight=1)
        text = self.controller.gd.get_textchapter(self.player.current_chapter)
        print(len(text))
        t = customtkinter.CTkLabel(master=frame,
                                   text=text, font=self.controller.textfont, wraplength=826)
        t.grid(row=0, column=0, sticky="ew")

        # combat skill
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=2, column=0, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='HABILITE', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        text = self.player.combat_skill + self.player.combat_skill_bonus - self.player.combat_skill_malus
        t = customtkinter.CTkLabel(master=frame,
                                   text=text, font=self.controller.textfont)
        t.grid(row=1, column=0, sticky="ew", padx=20)

        # Endurance
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=2, column=1, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='ENDURANCE', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        text = f'{self.player.endurance} / {self.player.endurance_max}'
        t = customtkinter.CTkLabel(master=frame,
                                   text=text, font=self.controller.textfont)
        t.grid(row=1, column=0, sticky="ew", padx=20)

        # meals
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=2, column=2, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='REPAS', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        t = customtkinter.CTkLabel(master=frame,
                                   text=self.player.meals, font=self.controller.textfont)
        t.grid(row=1, column=0, sticky="ew", padx=20)

        # belt pouch
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=2, column=3, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='BOURSE', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        pos = 1
        for key, value in self.player.belt_pouch.items():
            t = customtkinter.CTkLabel(master=frame,
                                       text=f"{key}: {value}", font=self.controller.textfont)
            t.grid(row=pos, column=0, sticky="ew", padx=20, pady=2)
            pos += 1

        # Kai Disciplines
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='DISCIPLINES KAI', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=(0, 10))
        pos = 1
        for kd in self.player.kai_discipline:
            if kd == 'Maîtrise des armes':
                text = self.player.weapon_skill_text()
            else:
                text = kd
            t = customtkinter.CTkLabel(master=frame,
                                       text=text, font=self.controller.textfont)
            t.grid(row=pos, column=0, sticky="ew", padx=20, pady=(0, 5))
            pos += 1

        # Weapons
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=3, column=2, columnspan=2, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='ARMES', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        if self.player.weapon1 != '':
            t = customtkinter.CTkLabel(master=frame,
                                       text=self.player.weapon1, font=self.controller.textfont, wraplength=400)
            t.grid(row=1, column=0, sticky="ew", padx=20, pady=2)
        if self.player.weapon2 != '':
            t = customtkinter.CTkLabel(master=frame,
                                       text=self.player.weapon2, font=self.controller.textfont, wraplength=400)
            t.grid(row=2, column=0, sticky="ew", padx=20, pady=2)
        if self.player.weapon1 == '' and self.player.weapon2 == '':
            text = "Combat livré sans arme : -4 points d'habilité"
        elif self.player.weapon_skill in (self.player.weapon1, self.player.weapon2):
            text = "Arme équipée avec la discipline kai maîtrise d'armes : +2 points d'habilité"
        else:
            text = ''
        if text != '':
            t = customtkinter.CTkLabel(master=frame,
                                       text=text, font=self.controller.textfont, wraplength=400, fg_color="#8c3430")
            t.grid(row=3, column=0, sticky="ew", padx=20)

        # backpack Items
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='SAC A DOS', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20)


        # special items
        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.grid(row=5, column=2, columnspan=2, sticky="ew", pady=10)
        frame.grid_columnconfigure(0, weight=1)
        t = customtkinter.CTkLabel(master=frame,
                                   text='OBJETS SPECIAUX', font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20)


