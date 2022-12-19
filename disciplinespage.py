import customtkinter

class DisciplinePage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent, width=900)

        self.controller = controller
        self.id = controller.id

        self.player = self.controller.player

        self.grid_columnconfigure(0, weight=1)

        self.create_widget()

    def create_widget(self):

        text = f"Au cours des siècles, les Moines Kaï ont appris à maîtriser toutes les techniques du guerrier." \
                f"Ces techniques sont connues sous le nom de Disciplines Kaï et enseignées aux seigneurs Kaï. " \
                f"Vous avez été initié à {len(self.player.kai_discipline)} des techniques décrites ci-dessous." \
                f"Il vous appartient de choisir vous-même ces disciplines limitées au nombre de 5 lors de votre" \
                f"première aventure. Chaque discipline peut vous être utile à un moment ou à un autre de votre quête " \
                f"et votre choix devra être le plus judicieux possible : dans certaines circonstances, une habile " \
                f"mise en pratique de l'une de ces techniques peut vous sauver la vie. Les techniques apprises ne " \
                f"peuvent pas être remplacées."

        t = customtkinter.CTkLabel(master=self,
                                   text=text, font=self.controller.textfont, wraplength=826)
        t.grid(row=0, column=0, sticky="ew", padx=20)

        tabview = customtkinter.CTkTabview(master=self)
        tabview.grid(row=1, column=0, sticky="ew", padx=5)
        tab1 = tabview.add("1 à 5")
        tab2 = tabview.add("6 à 10")
        tabview.set("1 à 5")


        row = 0
        for key, value in self.controller.gd.kai_disciplines.items():
            if row < 5:
                t = customtkinter.CTkLabel(master=tab1,
                                           text=key, font=self.controller.textfont, wraplength=100)
                t.grid(row=row, column=0, sticky="ew", padx=5, pady=(5, 5))
                t = customtkinter.CTkLabel(master=tab1,
                                           text=value, font=self.controller.textfont, wraplength=700)
                t.grid(row=row, column=1, sticky="ew", padx=5, pady=(5, 5))
            else:
                t = customtkinter.CTkLabel(master=tab2,
                                           text=key, font=self.controller.textfont, wraplength=100)
                t.grid(row=row, column=0, sticky="ew", padx=5, pady=(5, 5))
                t = customtkinter.CTkLabel(master=tab2,
                                           text=value, font=self.controller.textfont, wraplength=700)
                t.grid(row=row, column=1, sticky="ew", padx=5, pady=(5, 5))
            row += 1

